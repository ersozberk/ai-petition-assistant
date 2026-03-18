# backend/main.py
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from app.core.security import PIIRedactor, PromptGuard
from app.schemas import PetitionRequest, PetitionResponse
from app.core.ai_service import generate_petition_text

app = FastAPI(title="AI Petition Assistant API", description="Tüketici Hakları Dilekçe Üreticisi")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Geliştirme aşamasında her şeye izin veriyoruz
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Güvenlik modüllerimizi başlatıyoruz
redactor = PIIRedactor()
guard = PromptGuard()

@app.post("/api/generate-petition", response_model=PetitionResponse)
def generate_petition(request: PetitionRequest):
    # 1. Güvenlik Katmanı: Prompt Injection Kontrolü
    if not guard.is_safe(request.user_complaint):
        raise HTTPException(status_code=400, detail="Güvenlik ihlali tespit edildi. Lütfen sadece şikayetinizi yazın.")

    # 2. Veri Mühendisliği: PII (Kişisel Veri) Maskeleme
    masked_text, mask_map = redactor.redact(request.user_complaint)

    # 3. Yapay Zeka: Dilekçe Üretimi (Maskelenmiş veri ile!)
    try:
        ai_generated_text = generate_petition_text(masked_complaint=masked_text, company_name=request.company_name)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Dilekçe üretilemedi: {str(e)}")

    # 4. Veri Mühendisliği: Orijinal PII Verilerini Geri Yükleme
    final_petition = redactor.restore(ai_generated_text, mask_map)

    return PetitionResponse(petition_text=final_petition, status="success")