# Step-by-step build guide

Do **one step**, check that it worked, then move on. If anything shows an
error, stop and send the full output to Claude.

All commands go in your **Ubuntu (WSL)** terminal.

---

## Before you start (one time): give WSL more memory

By default WSL only gets about half of your 8 GB. In **Windows PowerShell**:

```powershell
notepad "$env:USERPROFILE\.wslconfig"
```

Paste this, save and close Notepad:

```ini
[wsl2]
memory=6GB
swap=8GB
```

Then in PowerShell run `wsl --shutdown`, wait 10 seconds and reopen Ubuntu
(Docker Desktop may need restarting too).

---

## Step 1: Get the foundation onto your computer  ✅ files already built

```bash
cd ~
git clone https://github.com/<your-github-username>/bah-digital.git
cd ~/bah-digital
./scripts/setup.sh
```

**Expected:** green ✔ for Docker, Compose, openssl and memory, then
`.env created with random secrets`.

> Your passwords now live in `~/bah-digital/.env`. Never share or upload this file.

Check what is running (nothing yet, which is correct):

```bash
./scripts/health.sh
```

---

## Step 2: Start PostgreSQL (database)

```bash
docker compose up -d postgres
./scripts/health.sh
```

**Expected:** `● UP postgres`. The first start downloads about 150 MB.

Check that the service databases were created:

```bash
docker exec bah-postgres psql -U bah_admin -d bah -c '\l'
```

You should see `bah`, `n8n` and `litellm` in the list.

---

## Step 3: Start Qdrant (vector memory)

```bash
docker compose up -d qdrant
./scripts/health.sh
```

Open http://localhost:6333/dashboard. It asks for an API key: get it with
`grep QDRANT_API_KEY .env`.

---

## Step 4: Start Ollama and download your first local models

```bash
docker compose up -d ollama
./scripts/pull-models.sh
```

This downloads about 3 GB, so it takes a while. Then test it:

```bash
docker exec -it bah-ollama ollama run qwen3:4b "Say hello to Bah.Digital in one sentence"
```

On an 8 GB laptop expect a few words per second. That is normal: local
models handle private or simple work, and free cloud models handle heavy work.

---

## Step 5: Start Open WebUI (your AI chat screen)

```bash
docker compose up -d open-webui
```

Wait about a minute, then open http://localhost:3000.
**The first account you create becomes the admin.** Pick `qwen3:4b` and chat.

---

## Step 6: Start n8n (automation)

```bash
docker compose up -d n8n
```

Open http://localhost:5678 and create your owner account.

---

## Step 7: Get free cloud AI keys

All free, no credit card needed for these tiers (limits change, so check each site):

1. **Google AI Studio (Gemini):** https://aistudio.google.com/apikey
2. **Groq:** https://console.groq.com/keys
3. **OpenRouter** (free models): https://openrouter.ai/keys

Add them to `.env`:

```bash
nano .env
```

Fill in `GEMINI_API_KEY=`, `GROQ_API_KEY=` and `OPENROUTER_API_KEY=`, then
save with `Ctrl+O`, `Enter`, `Ctrl+X`.

> **Claude Pro has no API key.** Keep using Claude Pro yourself (claude.ai /
> Claude Code) as your senior engineer and strategist. A Claude **API** key is
> a separate pay-per-use product. Add one only when revenue justifies it.

---

## Step 8: Start the AI gateway (LiteLLM)

```bash
docker compose up -d litellm
./scripts/health.sh
```

Test the router by asking for a **job**, not a model:

```bash
source .env
curl -s http://localhost:4000/v1/chat/completions \
  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"bah-fast","messages":[{"role":"user","content":"Give me 3 business ideas for Freetown."}]}'
```

Restart Open WebUI so the gateway models (`bah-fast`, `bah-research`,
`bah-coding`) appear in its model list:

```bash
docker compose restart open-webui
```

---

## Step 9: First backup + first commit

```bash
./scripts/backup.sh
git add -A && git commit -m "Phase 1 running locally" && git push
```

🎉 **Phase 0 and Phase 1 are complete.** Next is Phase 3 (knowledge brain): see ROADMAP.md.
