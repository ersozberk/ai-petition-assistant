# Tüketici Hakları Yapay Zeka Dilekçe Asistanı

[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/ersozberk/ai-petition-assistant/edit/main/README.md)
[![pt-br](https://img.shields.io/badge/lang-tr-green.svg)](https://github.com/ersozberk/ai-petition-assistant/edit/main/README-tr.md)

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

git clone git clone https://github.com/ersozberk/ai-petition-assistant.git

```

2. .env dosyaları oluşturun:

backend/.env -> HUGGINGFACE_API_KEY=your_token

frontend/.env.local -> NEXT_PUBLIC_API_URL=http://localhost:8000

3. Çalıştırın Uygulama:

```bash
docker-compose up --build
```
4. http://localhost:3000 adresini ziyaret edin

