# ⚖️ AI Petition Assistant 


[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/ersozberk/ai-petition-assistant/edit/main/README.md)
[![pt-br](https://img.shields.io/badge/lang-tr-green.svg)](https://github.com/ersozberk/ai-petition-assistant/edit/main/README-tr.md)

A Full-Stack AI application designed for LegalTech. It generates formal consumer rights petitions using LLMs while strictly protecting Personally Identifiable Information (PII).

## Key Features & Engineering Highlights

* **🛡️ PII Redaction (Security):** Automatically detects and masks sensitive user data (National ID, Phone) before sending it to the AI model, restoring it locally before download.
* **🤖 AI Fallback Strategy:** Uses a robust AI service architecture that falls back across multiple models (Qwen, Mistral) via HuggingFace Inference API to ensure 100% uptime.
* **🐳 Dockerized:** Fully containerized Backend and Frontend. Can be spun up locally with a single `docker-compose up` command.
* **🧪 E2E Tested:** Automated user flow testing using **Playwright**.
* **⚡ Modern Stack:** Built with Next.js (TypeScript/Tailwind) and FastAPI (Python/Pydantic).

## Tech Stack
* **Frontend:** Next.js (App Router), TypeScript, TailwindCSS
* **Backend:** Python, FastAPI, HuggingFace `huggingface_hub`
* **DevOps & Testing:** Docker Compose, Playwright, Pytest

## Local Setup (Docker)

1. Clone the repository:
   ```bash
   git clone https://github.com/ersozberk/ai-petition-assistant.git
   ```

2. Create .env files:

backend/.env -> HUGGINGFACE_API_KEY=your_token

frontend/.env.local -> NEXT_PUBLIC_API_URL=http://localhost:8000

3. Run the application:

```bash
docker-compose up --build
```
4. Visit http://localhost:3000
