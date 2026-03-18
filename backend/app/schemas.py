# app/schemas.py
from pydantic import BaseModel, Field

class PetitionRequest(BaseModel):
    user_complaint: str = Field(..., min_length=10, description="Kullanıcının olayı anlattığı şikayet metni.")
    company_name: str = Field(..., description="Şikayet edilen firmanın adı.")

class PetitionResponse(BaseModel):
    petition_text: str
    status: str