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

function getSkillFiles() {
  return fs
    .readdirSync(SKILLS_DIR)
    .filter((f) => f.endsWith('.md') && f !== 'README.md')
    .sort();
}

function installTo(agent, destOverride) {
  const dest = destOverride || AGENT_DIRS[agent];
  if (!dest) {
    console.error(`Unknown agent "${agent}". Supported agents: ${SUPPORTED_AGENTS.join(', ')}`);
    process.exit(1);
  }

  fs.mkdirSync(dest, { recursive: true });

  const skills = getSkillFiles();
  let installed = 0;

  for (const file of skills) {
    const src = path.join(SKILLS_DIR, file);
    const dst = path.join(dest, file);
    fs.copyFileSync(src, dst);
    console.log(`  ✓ ${file}`);
    installed++;
  }

  console.log(`\nInstalled ${installed} skill(s) to ${dest}`);
}

function listSkills() {
  const skills = getSkillFiles();
  console.log(`\nJerry's Agent Skills (${skills.length} total)\n`);

  const stateMachine = skills.filter((f) => f.includes('state-machine'));
  const conceptual = skills.filter((f) => !f.includes('state-machine'));

  console.log('Operational Protocols / State-Machine Skills:');
  stateMachine.forEach((f) => console.log(`  ${f}`));

  console.log('\nConceptual / Framework Skills:');
  conceptual.forEach((f) => console.log(`  ${f}`));
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
  install   Copy skill .md files to the agent's skills directory
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
