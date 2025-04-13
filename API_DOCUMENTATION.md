# Indian Languages Translator API Documentation

## Base URL
```
https://indian-languages-translator-xxxx.onrender.com
```

## Endpoints

### 1. Health Check
Check if the API is running properly.

**Endpoint:** `GET /health`

**Response:**
```json
{
    "status": "healthy"
}
```

### 2. Welcome Page
Get information about supported languages and API status.

**Endpoint:** `GET /`

**Response:**
```json
{
    "message": "Welcome to Indian Languages Translator API",
    "supported_languages": {
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
}
```

### 3. Translate Text
Translate text between English and Indian languages.

**Endpoint:** `POST /translate`

**Request Body:**
```json
{
    "text": "Hello, how are you?",
    "target_language": "hi",
    "source_language": "en"
}
```

**Parameters:**
- `text` (string, required): The text to translate
- `target_language` (string, required): The language code to translate to
- `source_language` (string, optional): The language code of the source text (defaults to "en")

**Language Codes:**
- `en`: English
- `hi`: Hindi
- `ta`: Tamil
- `te`: Telugu
- `ml`: Malayalam
- `kn`: Kannada
- `bn`: Bengali
- `gu`: Gujarati
- `mr`: Marathi
- `pa`: Punjabi
- `ur`: Urdu

**Response:**
```json
{
    "translated_text": "नमस्ते, आप कैसे हैं?",
    "source_language": "en",
    "target_language": "hi"
}
```

**Error Responses:**
```json
{
    "detail": "Unsupported target language. Supported languages are: ['hi', 'ta', 'te', 'ml', 'kn', 'bn', 'gu', 'mr', 'pa', 'ur'] and 'en'"
}
```
or
```json
{
    "detail": "Internal server error"
}
```

## Examples

### Using cURL

1. Health Check:
```bash
curl https://indian-languages-translator-xxxx.onrender.com/health
```

2. Get Welcome Page:
```bash
curl https://indian-languages-translator-xxxx.onrender.com/
```

3. Translate Text:
```bash
curl -X POST https://indian-languages-translator-xxxx.onrender.com/translate \
-H "Content-Type: application/json" \
-d '{
    "text": "Hello, how are you?",
    "target_language": "hi",
    "source_language": "en"
}'
```

### Using Python

```python
import requests

# Base URL
base_url = "https://indian-languages-translator-xxxx.onrender.com"

# Health check
response = requests.get(f"{base_url}/health")
print(response.json())

# Get welcome page
response = requests.get(base_url)
print(response.json())

# Translate text
translate_data = {
    "text": "Hello, how are you?",
    "target_language": "hi",
    "source_language": "en"
}
response = requests.post(f"{base_url}/translate", json=translate_data)
print(response.json())
```

### Using JavaScript/Fetch

```javascript
// Base URL
const baseUrl = 'https://indian-languages-translator-xxxx.onrender.com';

// Health check
fetch(`${baseUrl}/health`)
  .then(response => response.json())
  .then(data => console.log(data));

// Get welcome page
fetch(baseUrl)
  .then(response => response.json())
  .then(data => console.log(data));

// Translate text
fetch(`${baseUrl}/translate`, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    text: 'Hello, how are you?',
    target_language: 'hi',
    source_language: 'en'
  })
})
  .then(response => response.json())
  .then(data => console.log(data));
```

## Error Codes
- 400: Bad Request (invalid parameters)
- 500: Internal Server Error

## Support
For any issues or questions, please contact support or raise an issue in the GitHub repository. 