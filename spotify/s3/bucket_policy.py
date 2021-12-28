import json
import os
import boto3
from dotenv import load_dotenv


# Load enviromental variables
load_dotenv()
access_key = os.getenv('access_key')
access_secret = os.getenv('access_secret')
bucket_name = os.getenv('bucket_name')
account_id = os.getenv('account_id')


def main():

    # Bucket policy object

    bucket_policy = {
        'Version': '2012-10-17',
        'Statement': [
            {
                'Sid': 'AddPerm',
                'Effect': 'Allow',
                'Principal': {
                    'AWS': f'arn:aws:iam::{account_id}:root'
                },
                'Action': ['s3:GetObject'],
                'Resource': f'arn:aws:s3:::{bucket_name}/*'
            }]
    }

    # Convert policy from JSON dict to string
    bucket_policy = json.dumps(bucket_policy)

    # Set the new policy
    s3 = boto3.client(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=access_secret
    )
    s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)


if __name__ == '__main__':
    main()
