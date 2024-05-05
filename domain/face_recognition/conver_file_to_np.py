from PIL import Image
import io
import numpy as np


async def convert_file_to_np(file):
    file_data = await file.read()
    image = Image.open(io.BytesIO(file_data))
    return np.array(image)
