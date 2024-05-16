from deepface import DeepFace


def recognize_face(image_np):
    return DeepFace.analyze(img_path=image_np, actions=['age'], detector_backend='yolov8', enforce_detection=False)