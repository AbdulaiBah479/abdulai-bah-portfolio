# 01. Setup on Windows 11 (step by step)

Your other project (`../bah-digital/CLAUDE.md`) says you use **Windows 11 + WSL2 (Ubuntu) + Docker Desktop with 8 GB RAM**. These steps assume that. Commands change over time: if one fails, check the official docs at https://code.claude.com/docs and ask Claude to help.

## What each thing is (30-second version)
- **WSL2/Ubuntu**: a Linux "mini-computer" inside Windows. Most developer tools run best there.
- **Terminal**: the black window where you type commands.
- **Git**: tracks versions of files, like "Save history" for a project.
- **GitHub**: a website that stores your Git projects online (your backup).
- **Claude Code**: the AI assistant that runs in the terminal and can read and write files in a folder.

## Step 1. Open Ubuntu
Press the Windows key, type `Ubuntu`, press Enter. (If you have no Ubuntu, open PowerShell as Administrator, run `wsl --install`, restart, then open Ubuntu.)

## Step 2. Check git
```bash
git --version
```
If missing: `sudo apt update && sudo apt install -y git` (enter your Windows password if asked; nothing shows while typing, that is normal).

## Step 3. Install Claude Code
Official installer (check the docs page above for the current command):
```bash
curl -fsSL https://claude.ai/install.sh | bash
```
Then close and reopen Ubuntu and run `claude --version`. You need a Claude account (Pro or higher, or an API/Console account) to log in the first time. A browser window will open for login.

## Step 4. Get this project
```bash
cd ~
git clone -b ccr-d9fbef95-bc3hiy https://github.com/AbdulaiBah479/abdulai-bah-portfolio.git
cd abdulai-bah-portfolio/freelance-hq
```
(When you merge the branch into `main`, you can clone without `-b ...`.)

## Step 4b. Create your private tracker files
```bash
bash scripts/init_tracker.sh
```
This repo is **public** on GitHub, so your leads, income and drafts are kept in files Git ignores. Back them up somewhere private (e.g. a private repo or cloud drive), never in this public one.

## Step 5. Start Claude in this folder
```bash
claude
```
The first time it asks if you trust the folder: read, then say yes. Now try `/start`.

## Step 6. Install the small helpers (optional, later)
```bash
sudo apt install -y pandoc python3        # ebook builds + income report
```
Only install more when a task needs it (8 GB RAM is limited).

## Keeping your work safe
```bash
git add -A && git commit -m "Update trackers" && git push
```
Do this at the end of each work day. **Never commit client files**; `clients/` is already ignored by Git.

## Permissions: what Claude asks you
Claude will ask before editing files or running commands. Read what it wants to do. Say yes for things you understand (writing a file in this folder). Say no, and ask "why?", for anything that: spends money, sends emails/messages, deletes files, touches folders outside this project, or you do not understand.

## If something breaks
1. Copy the exact error text.
2. Paste it to Claude: "I ran X and got this error. Explain it simply and fix it."
3. If still stuck, search the exact error message in quotes online.
