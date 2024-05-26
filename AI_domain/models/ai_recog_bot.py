from openai import OpenAI
from .model_manage import GPT4O
import os

from dotenv import load_dotenv, find_dotenv
import os

_ = load_dotenv(find_dotenv())

key = os.getenv("OPENAI_API_KEY_EUNHAK")

client = OpenAI(api_key=key)


class faceRecog:
    def create_msg(base64_string):
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "You are an age classifier. Look at the face of the person in the front of the photo and You MUST respond only int: 1 for young, 2 for middle-aged, 3 for elderly, 0 if face is not recognized."},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpg;base64,{base64_string}"
                        }
                    }
                ]
            }
        ]
        return messages

    async def request_opt(msg):
        response = client.chat.completions.create(
            model=GPT4O,
            messages=msg,
            temperature=0,
        )
        return response.choices[0].message.content


