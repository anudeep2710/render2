# Indian Languages Translator API

A FastAPI-based translation service that supports translation between English and various Indian languages.

## Features

- Translation between English and 10 Indian languages
- Simple REST API interface
- Fast and reliable translations using Google Translate
- Support for language detection

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

## Installation

1. Clone the repository:
```bash
git clone https://github.com/anudeep2710/render2.git
cd render2
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the server:
```bash
python main.py
```

2. The API will be available at `http://localhost:8000`

### API Endpoints

- GET `/`: Welcome message and supported languages
- POST `/translate`: Translate text between languages

### Example Request

```json
{
    "text": "Hello, how are you?",
    "target_language": "hi",
    "source_language": "en"
}
```

### Example Response

```json
{
    "translated_text": "नमस्ते, आप कैसे हैं?",
    "source_language": "en",
    "target_language": "hi"
}
```

## License

MIT License 