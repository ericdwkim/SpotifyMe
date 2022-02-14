# NOTE: stores & downloads local audio files to AWS s3 bucket

import os
import logging
import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv


# Load enviromental variables
load_dotenv()
access_key = os.getenv('access_key')
access_secret = os.getenv('access_secret')
bucket_name = os.getenv('bucket_name')


def main():

    # Connect to S3 Service
    s3_client = boto3.client(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=access_secret
    )

    # Connect to S3 Resource
    s3_rsrc = boto3.resource(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=access_secret
    )


    # Download all track files from S3 
    bucket =  s3_rsrc.Bucket(bucket_name)
    for track in bucket.objects.all():
        try:
            print('Downloading track:  {0}...'.format(track.key))
            s3_client.download_file(
                bucket_name, 
                track.key,
                os.path.join('./audio_tracks/download', track.key))
        
        except ClientError as e:
            logging.error(e)
            return False
    return True

if __name__ == '__main__':
    main()
