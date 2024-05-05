
import uuid
from dotenv import load_dotenv, find_dotenv
from domain.common.aws import Aws

_ = load_dotenv(find_dotenv())


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
        return Aws.save_audio_on_s3(audio_data=audio_data, key=key)