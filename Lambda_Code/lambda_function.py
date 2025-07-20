import base64
import boto3
import uuid

s3 = boto3.client('s3')
ses = boto3.client('ses')
BUCKET = 'adham-site-static-20250719'

SENDER = "adhamayad000@gmail.com"
RECIPIENT = "aboayad557@gmail.com"
SUBJECT = "New Uploaded Image Link"

def lambda_handler(event, context):
    try:
        body = base64.b64decode(event['body'])
        content_type = event['headers'].get('Content-Type') or event['headers'].get('content-type')

        if not content_type.startswith("multipart/form-data"):
            return {
                "statusCode": 400,
                "body": '{"error":"Invalid content type"}'
            }

        boundary = content_type.split("boundary=")[-1]
        parts = body.split(boundary.encode())

        for part in parts:
            if b'filename=' in part:
                file_data = part.split(b'\r\n\r\n', 1)[1].rsplit(b'\r\n', 1)[0]
                file_name = str(uuid.uuid4()) + ".jpg"
                
                s3.put_object(Bucket=BUCKET, Key=file_name, Body=file_data, ContentType='image/jpeg')
                file_url = f"https://{BUCKET}.s3.amazonaws.com/{file_name}"

                # إرسال الإيميل
                ses.send_email(
                    Source=SENDER,
                    Destination={'ToAddresses': [RECIPIENT]},
                    Message={
                        'Subject': {'Data': SUBJECT},
                        'Body': {
                            'Text': {
                                'Data': f"The uploaded image is available at:\n{file_url}"
                            }
                        }
                    }
                )

                return {
                    "statusCode": 200,
                    "headers": {
                        "Access-Control-Allow-Origin": "*",
                        "Content-Type": "application/json"
                    },
                    "body": f'{{"imageUrl": "{file_url}"}}'
                }

        return {
            "statusCode": 400,
            "body": '{"error": "No file found in form data"}'
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": '{"error": "Internal Server Error"}'
        }
