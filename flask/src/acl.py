import boto3
import os
from dotenv import load_dotenv

# Load env vars
load_dotenv()
access_key = os.getenv('access_key')
access_secret = os.getenv('access_secret')
s3_bucket = os.getenv('bucket_name')


def main():

    # retrieve a s3 bucket's ACL
    s3 = boto3.client(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=access_secret
    )

    # s3 = boto3.client('s3')
    result = s3.get_bucket_acl(Bucket=s3_bucket)
    # print(type(result))
    print(result)


if __name__ == '__main__':
    main()
