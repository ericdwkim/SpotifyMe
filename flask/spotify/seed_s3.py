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
    s3 = boto3.client(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=access_secret
    )

    # Upload Files to S3
    data_file_path = os.path.join(os.getcwd(), 'audio_tracks')
    for file in os.listdir(data_file_path):
        if not file.startswith('~'):
            try:
                print('Uploading file {0}...'.format(file))
                s3.upload_file(
                    os.path.join(data_file_path, file),
                    bucket_name,
                    file
                )
            except ClientError as e:
                # print(f'Credential is incorrect' + e)
                logging.error(e)
                return False
            return True

    # Downloading Files from S3
    # TODO: programmatically fetch all keys from each s3 object to download in mass

    # s3.download_file(bucket_name, 'someTrack1.mp3',
    #                  os.path.join('./audio_tracks/download', 'test.mp3'))
    # s3.download_file(bucket_name, 'someTrack2.mp3',
    #                  os.path.join('./audio_tracks/download', 'test2.mp3'))


if __name__ == '__main__':
    main()

# TODO: IsADirectoryError: [Errno 21] Is a directory: '/Users/ekim/Code/SpotifyMe/flask/spotify/audio_tracks/download'
