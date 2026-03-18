# backend/Dockerfile
FROM python:3.10-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Sadece gereksinimleri kopyala (Cache optimizasyonu için)
COPY requirements.txt .

# Kütüphaneleri kur
RUN pip install --no-cache-dir -r requirements.txt

# Tüm kodları kopyala
COPY . .

# Uvicorn portunu dışarı aç
EXPOSE 8000

# Sunucuyu başlat (host 0.0.0.0 olmalı ki Docker dışından erişilebilsin)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]