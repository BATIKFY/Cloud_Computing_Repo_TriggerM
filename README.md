# API Documentation / Spec
# 1. Trigger ML Scan Batik
## Scan Batik
- Method : POST
- Endpoint : `https://trigger-gx62wmm6uq-et.a.run.app/process-image`
- Request Body :
```json 
{
    "image": "FILE"
}
```
- Response Body : 
```json 
{
    "confidence": "INTEGER",
    "predicted_class": "STRING"
}
```