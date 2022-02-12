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

    s3_rsrc = boto3.resource(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=access_secret
    )


    # Download Files from S3 en mass

    dl_file_path = os.path.join('./audio_tracks/download')
    bucket =  s3_rsrc.Bucket(bucket_name)

    for track in bucket.objects.all():
        try:
            print('Downloading file {0}...'.format(track))
            s3_client.download_file(
                bucket_name, 
                track.key,
                # dl_file_path)
                os.path.join('./audio_tracks/download', track.key))
        
        except ClientError as e:
            logging.error(e)
            return False
    return True

"""    
@dev: Downloads Files from S3
FEATURE_TODO: programmatically fetch all keys from each s3 object to download in mass
"""
    # s3.download_file(bucket_name, 'someTrack1.mp3',
    #                  os.path.join('./audio_tracks/download', 'test.mp3'))
    # s3.download_file(bucket_name, 'someTrack2.mp3',
    #                  os.path.join('./audio_tracks/download', 'test2.mp3'))


if __name__ == '__main__':
    main()
