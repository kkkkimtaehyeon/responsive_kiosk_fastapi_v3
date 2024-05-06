# import cv2
from deepface import DeepFace
from PIL import Image
import io
import numpy as np

def convert_jpg_to_np(file):
    contents = file.read()
    image = Image.open(io.BytesIO(contents))
    return np.array(image)

def get_age_from_image(image_np):
    result = DeepFace.analyze(img_path=image_np, actions=['age'], detector_backend='yolov8', enforce_detection=False)
    age = result[0]['age']
    return age


def determine_generation(age):
    if 0 <= age <= 40:
        return 'young'
    elif 40 < age <= 60:
        return 'middle'
    return 'old'
