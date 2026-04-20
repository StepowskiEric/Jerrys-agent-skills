#!/usr/bin/env node

'use strict';

const fs = require('fs');
const path = require('path');
const os = require('os');

// Skills directory: when installed via npx, __dirname is inside the package.
// When run locally from the repo root, __dirname is the bin/ folder.
const SKILLS_DIR = path.resolve(__dirname, '..');

const AGENT_DIRS = {
  codex: path.join(os.homedir(), '.codex', 'skills'),
  hermes: path.join(os.homedir(), '.hermes', 'skills'),
  claude: path.join(os.homedir(), '.claude', 'skills'),
  antigravity: path.join(os.homedir(), '.antigravity', 'skills'),
};

const SUPPORTED_AGENTS = Object.keys(AGENT_DIRS);

function getSkillFiles(dir, base) {
  base = base || dir;
  let results = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.isDirectory()) {
      results = results.concat(getSkillFiles(path.join(dir, entry.name), base));
    } else if (entry.name.endsWith('.md') && entry.name !== 'README.md') {
      results.push(path.relative(base, path.join(dir, entry.name)));
    }
  }
  return results.sort();
}

function getSkillBundlePath(file) {
  return path.join(path.dirname(file), path.basename(file, '.md'), 'SKILL.md');
}

function installTo(agent, destOverride) {
  const dest = destOverride || AGENT_DIRS[agent];
  if (!dest) {
    console.error(`Unknown agent "${agent}". Supported agents: ${SUPPORTED_AGENTS.join(', ')}`);
    process.exit(1);
  }

  fs.mkdirSync(dest, { recursive: true });

  const skills = getSkillFiles(SKILLS_DIR);
  let installed = 0;

  for (const file of skills) {
    const src = path.join(SKILLS_DIR, file);
    const dst = path.join(dest, getSkillBundlePath(file));
    fs.mkdirSync(path.dirname(dst), { recursive: true });
    fs.copyFileSync(src, dst);
    console.log(`  ✓ ${getSkillBundlePath(file)}`);
    installed++;
  }

  console.log(`\nInstalled ${installed} skill(s) to ${dest}`);
}

const TOPIC_DIRS = [
  'execution',
  'judgment-and-routing',
  'output-quality',
  'systems-and-architecture',
  'orchestration',
];

const TOPIC_LABELS = {
  'execution': 'Execution — how-to-do-the-work protocols',
  'judgment-and-routing': 'Judgment & Routing — deciding what to do and how rigorously',
  'output-quality': 'Output Quality — improving what the agent produces',
  'systems-and-architecture': 'Systems & Architecture — thinking about structure and scale',
  'orchestration': 'Orchestration — agent coordination and workflow control',
};

function listSkills() {
  const all = getSkillFiles(SKILLS_DIR);
  console.log(`\nJerry's Agent Skills (${all.length} total)\n`);

  for (const topic of TOPIC_DIRS) {
    const files = all.filter((f) => f.startsWith(topic + path.sep) || f.startsWith(topic + '/'));
    if (files.length === 0) continue;
    console.log(`${TOPIC_LABELS[topic] || topic}:`);
    for (const f of files) {
      const tag = f.includes('state-machine') ? ' [protocol]' : ' [framework]';
      console.log(`  ${f}${tag}`);
    }
    console.log('');
  }

  // Catch any files not in a known topic dir (e.g. root-level extras)
  const categorized = TOPIC_DIRS.flatMap((t) =>
    all.filter((f) => f.startsWith(t + path.sep) || f.startsWith(t + '/'))
  );
  const uncategorized = all.filter((f) => !categorized.includes(f));
  if (uncategorized.length > 0) {
    console.log('Other:');
    uncategorized.forEach((f) => console.log(`  ${f}`));
    console.log('');
  }
}

function printHelp() {
  console.log(`
jerry-skills — install Jerry's agent skill files into your AI agent

Usage:
  npx jerry-skills install --agent <name> [--dest <path>]
  npx jerry-skills install --all [--dest <path>]
  npx jerry-skills list
  npx jerry-skills help

Commands:
  install   Copy skill bundles to the agent's skills directory
  list      List all available skill files
  help      Show this help message

Options:
  --agent   Target agent: ${SUPPORTED_AGENTS.join(', ')}
  --all     Install to all supported agents
  --dest    Override the destination directory

Default install paths:
${SUPPORTED_AGENTS.map((a) => `  ${a.padEnd(12)} ${AGENT_DIRS[a]}`).join('\n')}

Examples:
  npx jerry-skills install --agent codex
  npx jerry-skills install --agent claude --dest ~/my-skills
  npx jerry-skills install --all
  npx jerry-skills list
`);
}

function main() {
  const args = process.argv.slice(2);
  const command = args[0];

  if (!command || command === 'help' || command === '--help' || command === '-h') {
    printHelp();
    return;
  }

  if (command === 'list') {
    listSkills();
    return;
  }

  if (command === 'install') {
    const agentIdx = args.indexOf('--agent');
    const allFlag = args.includes('--all');
    const destIdx = args.indexOf('--dest');
    const destOverride = destIdx !== -1 ? args[destIdx + 1] : null;

    if (allFlag) {
      console.log("Installing skills to all supported agents...\n");
      for (const agent of SUPPORTED_AGENTS) {
        console.log(`[${agent}]`);
        installTo(agent, destOverride ? path.join(destOverride, agent) : null);
        console.log('');
      }
      return;
    }

    if (agentIdx === -1 || !args[agentIdx + 1]) {
      console.error('Error: --agent <name> is required, or use --all.\n');
      printHelp();
      process.exit(1);
    }

    const agent = args[agentIdx + 1];
    if (!SUPPORTED_AGENTS.includes(agent)) {
      console.error(`Unknown agent "${agent}". Supported: ${SUPPORTED_AGENTS.join(', ')}`);
      process.exit(1);
    }

    console.log(`Installing skills for ${agent}...\n`);
    installTo(agent, destOverride);
    return;
  }

  console.error(`Unknown command "${command}".\n`);
  printHelp();
  process.exit(1);
}

main();
