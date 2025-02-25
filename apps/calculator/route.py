from fastapi import APIRouter
import base64
from io import BytesIO
from apps.calculator.utils import analyze_image
from schema import ImageData
from PIL import Image

router = APIRouter()

@router.post('')

async def run(data: ImageData):
    image_data = base64.b64decode(data.image.split(',')[1])
    image_bytes = BytesIO(image_data)
    image = Image.open(image_bytes)
    responses = analyze_image(image, dict_of_vars = data.dict_of_vars)
    data = []
    for responses in responses:
        data.append(responses)
    print('response in route: ', responses)
    return{
        "message": "Image Processed",
        "type": "success",
        "data": data,
    }