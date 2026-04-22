---
name: purify-test-output
description: Slice failing test output to only failure-relevant lines before showing to the LLM. Removes noise, reduces tokens by ~18.6%, and focuses attention on the actual bug. Based on DebugRepair research.
category: debugging
priority: high
tags: [testing, token-efficiency, debugging, test-output]
---

## Overview

Raw test output is noisy. A failing test may produce hundreds of lines of logs, stack traces through framework internals, and irrelevant setup output. The LLM's attention scatters across this noise, missing the actual signal.

**Test Semantic Purification** extracts only the failure-relevant context:
- The assertion that failed
- The stack trace frames in user code (not framework internals)
- The specific exception message
- Relevant variable values at the failure point

Research shows this reduces token count by **18.6%** on average and improves repair correctness.

## When to use

- Failing test produces verbose output (>20 lines)
- Stack trace includes framework/library frames that drown out user code
- Multiple tests fail and you need to isolate the most relevant failure first

## When NOT to use

- Test output is already minimal (single assertion failure)
- The bug is in the test itself (you need full test context)

## Core protocol

### Step 1 — Run the test and capture raw output

```bash
pytest test_foo.py -x --tb=long 2>&1 | tee /tmp/raw_output.txt
```

### Step 2 — Extract the failure signature

```python
# Pseudo-code for purification logic
def purify_test_output(raw_output):
    lines = raw_output.split('\n')
    purified = []
    in_user_trace = False

    for line in lines:
        # Keep assertion failure line
        if 'AssertionError' in line or 'FAILED' in line:
            purified.append(line)
            continue

        # Keep user-code stack frames (skip framework internals)
        if 'File "' in line:
            if 'site-packages' in line or 'lib/python' in line:
                in_user_trace = False
            else:
                in_user_trace = True

        if in_user_trace:
            purified.append(line)

        # Keep variable diff lines
        if line.startswith('E   ') or '==' in line or '!=' in line:
            purified.append(line)

    return '\n'.join(purified)
```

### Step 3 — Present purified output to LLM

```markdown
Test `test_process_order` failed. Purified output:

```
AssertionError: Expected 85.0 but got 100
  File "orders.py", line 14, in process_order
  File "payments.py", line 7, in charge_customer
KeyError: 'id'
```
```

## Rules for purification

| Keep | Discard |
|------|---------|
| Assertion message | Test setup/teardown logs |
| User-code stack frames | Framework internal frames |
| Exception type and message | Pass/skip summaries for other tests |
| Variable diffs (`expected X, got Y`) | Coverage reports |
| Last 3 lines of stderr | stdout from passing tests |

## Research basis

- **DebugRepair** (arXiv:2604.19305): Test semantic purification reduces runtime output tokens by **18.6%**.
- Ablation: removing purification caused a **26.8% drop** in correct fixes.
- The slicing is based on data and control dependencies from the failing assertion backward.

## Example

**Raw output (47 lines):**
```
============================= test session starts ==============================
platform darwin -- Python 3.14.4
rootdir: /tmp/project
collected 3 items

test_order.py::test_process_order FAILED

test_order.py:15: in test_process_order
    result = process_order(order)
orders.py:14: in process_order
    charge_customer(order["customer"], total)
../../../opt/homebrew/lib/python3.14/site-packages/pytest/...
[... 30 more framework frames ...]
AssertionError: Expected 85.0 but got 100

========================= 1 failed, 2 passed ==========================
```

**Purified output (5 lines):**
```
test_order.py::test_process_order FAILED
AssertionError: Expected 85.0 but got 100
  File "orders.py", line 14, in process_order
  File "payments.py", line 7, in charge_customer
```

## Pitfalls

- **Over-purification**: Don't remove the test assertion line — it contains the expected vs actual values.
- **Under-purification**: Framework frames like `pytest.raises` or `asyncio.run` may be relevant if the bug involves async/test infrastructure.
- **Multi-failure cascades**: If test A fails because test B's setup broke, you may need both failure outputs.
