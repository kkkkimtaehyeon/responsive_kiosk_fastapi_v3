from AI_domain.models.ai_recog_bot import faceRecog


async def face_recog(base64_str):
    msg = faceRecog.create_msg(base64_str)
    generation_opt = await faceRecog.request_opt(msg)
    return generation_opt