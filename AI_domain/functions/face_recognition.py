from deepface import DeepFace

# 얼굴 인식 및 사람들 나이 추출
def recognize_face(image_np):
    return DeepFace.analyze(img_path=image_np, actions=['age'], detector_backend='yolov8', enforce_detection=False)