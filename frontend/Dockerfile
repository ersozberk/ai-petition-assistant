# frontend/Dockerfile
FROM node:20-alpine

# Çalışma dizinini ayarla
WORKDIR /app

# Paket dosyalarını kopyala
COPY package*.json ./

# Bağımlılıkları kur
RUN npm install

# Tüm kodları kopyala
COPY . .

# Üretim (Build) aşamasında Backend URL'ini veriyoruz
ENV NEXT_PUBLIC_API_URL=http://localhost:8000

# Next.js'i production için optimize et
RUN npm run build

# Portu dışarı aç
EXPOSE 3000

# Uygulamayı başlat
CMD ["npm", "start"]