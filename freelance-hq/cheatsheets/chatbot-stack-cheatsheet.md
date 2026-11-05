# Chatbot / RAG stack cheat sheet

## Concepts in plain words
- **LLM**: the language brain. **Prompt**: instructions. **Context window**: how much it can read at once.
- **RAG (retrieval-augmented generation)**: before answering, the bot searches your documents and feeds the best pieces to the LLM so it answers from facts.
- **Embedding**: turning text into numbers so similar meanings can be found.
- **Vector database**: stores embeddings (Qdrant, Chroma, pgvector).
- **Chunking**: splitting documents into small pieces (200-500 words) with titles.
- **Hallucination**: confident wrong answer. Fix with sources, "say I don't know", and testing.
- **Guardrails**: rules on what the bot may/may not say.

## Build ladder (start simple)
1. FAQ in the prompt (under ~30 Q&A) -> no database needed.
2. RAG with a vector DB for larger knowledge bases.
3. Add tools (booking, CRM) after the basics work.
4. Add analytics and review logs.

## Free/open tools to evaluate (check licences; see resources/github-repos.md)
Langflow, Dify, Open WebUI, LangChain/LangGraph, LlamaIndex, Qdrant/Chroma, markitdown/docling/unstructured (document conversion), faster-whisper (voice), promptfoo (testing prompts), Langfuse (observability). Flowise's GitHub repo is archived: verify status before using.

## Prompt skeleton
```
You are the assistant for [Business]. Answer ONLY from the provided sources.
If the answer isn't in the sources, say you don't know and offer [contact].
Tone: [friendly/professional]. Language: [..]. Keep answers under [N] sentences.
Never give medical/legal/financial advice. Never invent prices or policies.
Collect leads only when the user agrees: name + email/phone.
```

## Testing
30+ questions: normal, tricky, off-topic, rude, multilingual. Score correctness, tone, citation. Keep a spreadsheet; retest after every change.

## Privacy and cost
Tell users it's an AI, avoid collecting sensitive data, store logs only with consent, explain API cost per conversation to the client, set rate limits.

## Channels
Website widget, Telegram, Messenger, email. WhatsApp requires Business API approval and has conversation fees (verify) before you promise it.
