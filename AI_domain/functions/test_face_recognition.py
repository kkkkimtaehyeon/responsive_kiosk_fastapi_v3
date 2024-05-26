from AI_domain.models.ai_recognition_bot import faceRecognition


async def face_recognition(base64_str):
    message = faceRecognition.create_message(base64_str)
    generation_option = await faceRecognition.request_option(message)
    return generation_option