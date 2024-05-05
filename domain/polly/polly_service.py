import boto3
import os
import uuid
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

BUCKET = 'responsive-bucket'
REGION = 'ap-northeast-2'


class Aws:
    # polly 접근
    polly = boto3.client(
        'polly',
        aws_access_key_id=os.getenv("S3_ACCESS_KEY"),
        aws_secret_access_key=os.getenv("S3_SECRET_KEY"),
        region_name='ap-northeast-2'
    )

    # S3 접근
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.getenv("S3_ACCESS_KEY"),
        aws_secret_access_key=os.getenv("S3_SECRET_KEY")
    )


class PollyService:

    def get_tts_url(userScript):
        # 텍스트를 음성으로 변환
        response = Aws.polly.synthesize_speech(
            LanguageCode='ko-KR',
            Text=userScript,
            OutputFormat='mp3',
            VoiceId='Seoyeon'
        )

        # 스트림에서 바이트 데이터 읽기
        audio_data = response['AudioStream'].read()

        key = f'{uuid.uuid4()}_tts.wav'
        #key = 'test.wav'

        # 바이트 데이터를 S3에 업로드
        Aws.s3.put_object(Body=audio_data, Bucket='responsive-bucket', Key=key, ContentType='audio/wav')

        return f'https://{BUCKET}.s3.{REGION}.amazonaws.com/{key}'
