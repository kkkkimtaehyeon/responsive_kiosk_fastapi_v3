# import cv2
from PIL import Image
import io
import numpy as np

from AI_test.face_recognition.face_recognition import recognize_face

def convert_jpg_to_np(file):
    contents = file.read()
    image = Image.open(io.BytesIO(contents))
    return np.array(image)

def get_age_from_image(image_np):
    result = recognize_face(image_np)
    age = result[0]['age']
    return age


def determine_generation(age):
    if 0 <= age <= 40:
        return 'young'
    elif 40 < age <= 60:
        return 'middle'
    return 'old'
