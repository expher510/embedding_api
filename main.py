from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoImageProcessor, AutoModel
import torch
from PIL import Image
import requests
from io import BytesIO
import uvicorn

app = FastAPI(title="Movie Linker - Image Embedding API (DINOv2)")

class ImageRequest(BaseModel):
    image_url: str

# Load Model
img_model_id = 'facebook/dinov2-base'
img_processor = AutoImageProcessor.from_pretrained(img_model_id)
img_model = AutoModel.from_pretrained(img_model_id)
img_model.eval()

@app.get("/")
def home():
    return {"status": "online", "model": img_model_id, "endpoint": "/embed/image"}

@app.post("/embed/image")
async def embed_image(request: ImageRequest):
    try:
        response = requests.get(request.image_url, timeout=10)
        img = Image.open(BytesIO(response.content)).convert("RGB")
        
        # Process image
        inputs = img_processor(images=img, return_tensors="pt")
        
        with torch.no_grad():
            outputs = img_model(**inputs)
            # Use CLS token for global representation (768 dimensions)
            embedding = outputs.last_hidden_state[:, 0, :].squeeze().tolist()
            
        return {
            "success": True, 
            "model": img_model_id,
            "dimension": len(embedding), 
            "embedding": embedding
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
