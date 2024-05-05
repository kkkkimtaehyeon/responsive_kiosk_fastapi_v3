# import cv2
from deepface import DeepFace


def get_age_from_image(image_np):
    result = DeepFace.analyze(image_np, actions=['age'], detector_backend='yolov8', enforce_detection=False)
    age = result[0]['age']
    return age


def determine_generation(age):
    if 0 <= age <= 40:
        return 'young'
    elif 40 < age <= 60:
        return 'middle'
    return 'old'
