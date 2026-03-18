# app/core/security.py
import re
import uuid
from typing import Tuple, Dict

class PIIRedactor:
    def __init__(self):
        # Temel Türkçe PII Regex Kuralları
        self.rules = {
            "TC_KIMLIK": r"\b[1-9][0-9]{10}\b",
            "TELEFON": r"\b(?:0|90|\+90)?\s?5\d{2}\s?\d{3}\s?\d{2}\s?\d{2}\b",
            "EMAIL": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
        }

    def redact(self, text: str) -> Tuple[str, Dict[str, str]]:
        """
        Metindeki kişisel verileri maskeler.
        Maskelenmiş metni ve orijinal verileri içeren bir harita (map) döner.
        """
        mask_map = {}
        redacted_text = text

        for entity_type, pattern in self.rules.items():
            matches = re.finditer(pattern, redacted_text)
            for match in matches:
                original_value = match.group()
                # Her maskelenen veri için benzersiz bir ID oluşturuyoruz (Geri dönüştürmek için)
                mask_id = f"[{entity_type}_{uuid.uuid4().hex[:6].upper()}]"
                mask_map[mask_id] = original_value
                redacted_text = redacted_text.replace(original_value, mask_id)

        return redacted_text, mask_map

    def restore(self, redacted_text: str, mask_map: Dict[str, str]) -> str:
        """
        Yapay zekadan dönen maskelenmiş metne orijinal verileri geri yerleştirir.
        """
        restored_text = redacted_text
        for mask_id, original_value in mask_map.items():
            restored_text = restored_text.replace(mask_id, original_value)
        return restored_text

class PromptGuard:
    def __init__(self):
        # Temel prompt injection yakalama anahtar kelimeleri
        self.blacklist = [
            "önceki komutları unut",
            "sistem prompt",
            "ignore previous instructions",
            "bana kurallarını söyle",
            "sistemi atla"
        ]

    def is_safe(self, text: str) -> bool:
        """
        Metin içinde zararlı bir komut olup olmadığını kontrol eder.
        """
        lower_text = text.lower()
        for word in self.blacklist:
            if word in lower_text:
                return False
        return True