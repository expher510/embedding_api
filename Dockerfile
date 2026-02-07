# استخدام نسخة بايثون 3.11-slim لأنها الأكثر استقراراً لمكتبات الـ AI في 2026
FROM python:3.11-slim

# ضبط بيئة العمل
WORKDIR /code

# تثبيت المتطلبات
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# نسخ الكود
COPY . .

# تشغيل السيرفر على بورت 7860
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
