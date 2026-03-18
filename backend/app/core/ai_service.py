# app/core/ai_service.py
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

# Profesyonel Yaklaşım: Birden fazla model deneme (Fallback Strategy)
# Qwen2.5 şu an dünyadaki en iyi açık kaynaklı modellerden biridir.
MODELS = [
    "Qwen/Qwen2.5-7B-Instruct", 
    "mistralai/Mistral-7B-Instruct-v0.3",
    "meta-llama/Llama-3.2-3B-Instruct"
]

def generate_petition_text(masked_complaint: str, company_name: str) -> str:
    prompt = f"""Sen uzman bir Türk tüketici hakları avukatısın. Aşağıdaki bilgilere dayanarak resmi bir Tüketici Hakem Heyeti dilekçesi yaz. 
    
Firma: {company_name}
Şikayet: {masked_complaint}

Lütfen sadece dilekçe metnini döndür, açıklama veya yorum yapma."""

    last_error = ""
    
    # Listedeki modelleri sırayla dener
    for model_id in MODELS:
        try:
            client = InferenceClient(model=model_id, token=os.getenv("HUGGINGFACE_API_KEY"))
            
            response = client.chat_completion(
                messages=[
                    {"role": "system", "content": "Sen sadece Türkçe hukuki dilekçe yazan bir asistansın."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1000,
                temperature=0.1 # Daha tutarlı ve resmi bir dil için düşürdük
            )
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            last_error = str(e)
            print(f"Model {model_id} başarısız oldu, diğeri deneniyor... Hata: {last_error}")
            continue # Hata alırsan döngüdeki bir sonraki modele geç
            
    # Eğer tüm modeller başarısız olursa
    raise Exception(f"Tüm AI modelleri denendi ancak yanıt alınamadı. Son hata: {last_error}")