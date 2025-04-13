from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from googletrans import Translator
from typing import Optional

app = FastAPI(title="Indian Languages Translator",
             description="Translate text between English and Indian languages")

# Initialize the translator
translator = Translator()

# Supported Indian languages
SUPPORTED_LANGUAGES = {
    "hi": "Hindi",
    "ta": "Tamil",
    "te": "Telugu",
    "ml": "Malayalam",
    "kn": "Kannada",
    "bn": "Bengali",
    "gu": "Gujarati",
    "mr": "Marathi",
    "pa": "Punjabi",
    "ur": "Urdu"
}

class TranslationRequest(BaseModel):
    text: str
    target_language: str
    source_language: Optional[str] = "en"

class TranslationResponse(BaseModel):
    translated_text: str
    source_language: str
    target_language: str

@app.get("/")
def read_root():
    return {"message": "Welcome to Indian Languages Translator API",
            "supported_languages": SUPPORTED_LANGUAGES}

@app.post("/translate", response_model=TranslationResponse)
def translate_text(request: TranslationRequest):
    try:
        # Validate target language
        if request.target_language not in SUPPORTED_LANGUAGES and request.target_language != "en":
            raise HTTPException(
                status_code=400,
                detail=f"Unsupported target language. Supported languages are: {list(SUPPORTED_LANGUAGES.keys())} and 'en'"
            )

        # Perform translation
        translation = translator.translate(
            text=request.text,
            src=request.source_language,
            dest=request.target_language
        )

        return TranslationResponse(
            translated_text=translation.text,
            source_language=translation.src,
            target_language=translation.dest
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
