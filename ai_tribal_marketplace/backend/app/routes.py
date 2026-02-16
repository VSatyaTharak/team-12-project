from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from PIL import Image
import io

from .database import SessionLocal, get_db
from .models import Product
from .services.vit_model import extract_features
from .services.text_generator import generate_description
from .services.translator import translate_text

router = APIRouter()

@router.post("/generate/")
async def generate(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))

        features = extract_features(image)
        english = generate_description(features)

        hindi = translate_text(english, "hi")
        maithili = translate_text(english, "mai")
        konkani = translate_text(english, "gom")

        product = Product(
            english=english,
            hindi=hindi,
            maithili=maithili,
            konkani=konkani
        )

        db.add(product)
        db.commit()

        return {
            "english": english,
            "hindi": hindi,
            "maithili": maithili,
            "konkani": konkani
        }
    except Exception as e:
        import traceback
        tb = traceback.format_exc()
        print(tb)
        raise HTTPException(status_code=500, detail=str(e))