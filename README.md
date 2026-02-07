# Moving Linking - Image Embedding API (DINOv2)

هذا الجزء من المشروع مسؤول عن تحويل صور الأفلام وصور اليوتيوب (Thumbnails) إلى بصمات رقمية (Vectors) باستخدام موديل **DINOv2** من فيسبوك.

## رابط السبيس (Hugging Face)
[aliSaac510/Embedding](https://huggingface.co/spaces/aliSaac510/Embedding)

---

## كيفية تجربة الـ API (PowerShell)

استخدم الأوامر التالية في الـ Terminal الخاص بالويندوز (PowerShell) للتأكد من أن السيرفر يعمل بشكل صحيح:

```powershell
# 1. تجهيز الرابط (استخدام i.ytimg.com لتجنب مشاكل الـ DNS)
$body = @{ image_url = "https://i.ytimg.com/vi/aqz-KE-bpKQ/hqdefault.jpg" } | ConvertTo-Json

# 2. إرسال الطلب واستقبال الفيكتور
Invoke-RestMethod -Uri "https://alisaac510-embedding.hf.space/embed/image" -Method Post -Body $body -ContentType "application/json"
```

### النتيجة المتوقعة:
سيرجع السيرفر JSON يحتوي على:
- `success`: true
- `dimension`: 768
- `embedding`: [قائمة طويلة من الأرقام]

---

## المكونات التقنية
- **Model**: `facebook/dinov2-base`
- **Framework**: FastAPI + Transformers
- **Python Version**: 3.11-slim
- **Target Dimensions**: 768 (يجب أن تتطابق مع أبعاد جدول Supabase)
