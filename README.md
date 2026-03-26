# ⚖️ AI Petition Assistant 
A production-ready Full-Stack AI application designed for LegalTech. It generates formal consumer rights petitions using LLMs while strictly protecting Personally Identifiable Information (PII).

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
   git clone [https://github.com/yourusername/ai-petition-assistant.git](https://github.com/yourusername/ai-petition-assistant.git)
   ```

2. Create .env files:

backend/.env -> HUGGINGFACE_API_KEY=your_token

frontend/.env.local -> NEXT_PUBLIC_API_URL=http://localhost:8000

3. Run the application:

```bash
docker-compose up --build
```
4. Visit http://localhost:3000


# Tüketici Hakları Yapay Zeka Dilekçe Asistanı

Adli teknoloji için tasarlanmış, üretime hazır, tam yığınlı bir yapay zeka uygulaması. Kişisel Tanımlanabilir Bilgileri (PII) kesinlikle korurken, LLM'leri kullanarak resmi tüketici hakları dilekçeleri oluşturur.

## Temel Özellikler ve Mühendislik Öne Çıkan Noktaları

* **🛡️ PII Gizleme (Güvenlik):** Hassas kullanıcı verilerini (Ulusal Kimlik, Telefon) yapay zeka modeline göndermeden önce otomatik olarak algılar ve maskeler, indirmeden önce yerel olarak geri yükler.

* **🤖 Yapay Zeka Yedekleme Stratejisi:** %100 çalışma süresi sağlamak için HuggingFace Çıkarım API'si aracılığıyla birden fazla model (Qwen, Mistral) arasında yedekleme yapan sağlam bir yapay zeka hizmet mimarisi kullanır.

* **🐳 Dockerize Edilmiş:** Tamamen konteynerleştirilmiş Arka Uç ve Ön Uç. Tek bir `docker-compose up` komutuyla yerel olarak çalıştırılabilir.
* **🧪 Uçtan Uca Test Edildi:** **Playwright** kullanılarak otomatik kullanıcı akışı testi yapıldı.

* **⚡ Modern Teknoloji Yığını:** Next.js (TypeScript/Tailwind) ve FastAPI (Python/Pydantic) ile geliştirildi.

## Teknoloji Yığını
* **Ön Uç:** Next.js (Uygulama Yönlendirici), TypeScript, TailwindCSS
* **Arka Uç:** Python, FastAPI, HuggingFace `huggingface_hub`
* **DevOps ve Test:** Docker Compose, Playwright, Pytest

## Yerel Kurulum (Docker)

1. Depoyu klonlayın:

```bash

git clone [https://github.com/yourusername/ai-petition-assistant.git](https://github.com/yourusername/ai-petition-assistant.git)

```

2. .env dosyaları oluşturun:

backend/.env -> HUGGINGFACE_API_KEY=your_token

frontend/.env.local -> NEXT_PUBLIC_API_URL=http://localhost:8000

3. Çalıştırın Uygulama:

```bash
docker-compose up --build
```
4. http://localhost:3000 adresini ziyaret edin

