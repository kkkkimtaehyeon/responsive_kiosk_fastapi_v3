import boto3
import os

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

    

    def save_image_on_s3(image_data, key):
        Aws.s3.put_object(Body=image_data, Bucket=BUCKET, Key=key, ContentType='image/jpg')
        return f'https://{BUCKET}.s3.{REGION}.amazonaws.com/{key}'
    
    def save_audio_on_s3(audio_data, key):
        Aws.s3.put_object(Body=audio_data, Bucket='responsive-bucket', Key=key, ContentType='audio/wav')
        return f'https://{BUCKET}.s3.{REGION}.amazonaws.com/{key}'