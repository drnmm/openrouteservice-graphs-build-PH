import boto3, os
from boto3.s3.transfer import TransferConfig

MB = 1024 ** 2

s3 = boto3.resource('s3',
  endpoint_url = os.getenv("S3_ENDPOINT"),
  aws_access_key_id = os.getenv("ACCESS_ID"),
  aws_secret_access_key = os.getenv("ACCESS_KEY")
)


try:
  s3.meta.client.upload_file("./docker/philippines-latest.zip", "ors-files", "philippines-latest.zip", 
    ExtraArgs={'ContentType':'application/x-zip-compressed'}, 
    Config=TransferConfig(multipart_threshold=100*MB, max_concurrency=3)
  )
  print("File 'philippines-latest.zip' successfully uploaded.")
except Exception as e:
  print(e)
  print("Upload failed")