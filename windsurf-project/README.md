# Indian Languages Translator API

A FastAPI-based translation service that supports translation between English and various Indian languages.

## Supported Languages

- Hindi (hi)
- Tamil (ta)
- Telugu (te)
- Malayalam (ml)
- Kannada (kn)
- Bengali (bn)
- Gujarati (gu)
- Marathi (mr)
- Punjabi (pa)
- Urdu (ur)

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
python main.py
```

The API will be available at http://localhost:8000

## API Usage

### 1. Get Supported Languages
GET `/`

### 2. Translate Text
POST `/translate`

Request body:
```json
{
    "text": "Hello, how are you?",
    "target_language": "hi",
    "source_language": "en"  // optional, defaults to "en"
}
```

Response:
```json
{
    "translated_text": "नमस्ते, आप कैसे हैं?",
    "source_language": "en",
    "target_language": "hi"
}
```
