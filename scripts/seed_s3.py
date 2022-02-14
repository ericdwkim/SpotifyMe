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
    # s3_rsrc = boto3.resource(
    #     's3',
    #     aws_access_key_id=access_key,
    #     aws_secret_access_key=access_secret
    # )
    # bucket =  s3_rsrc.Bucket(bucket_name)

    # Upload track files to S3 &&  grant READ only permissions to objects
    data_file_path = os.path.join(os.getcwd(), 'audio_tracks/upload')
    for track in os.listdir(data_file_path):
        if not track.startswith('~'):
            try:
                print('Uploading track:  {0}...'.format(track))
                s3_client.upload_file(
                    os.path.join(data_file_path, track),
                    bucket_name,
                    track,
                    ExtraArgs={
                        'ACL':'public-read'}
                )
            
            except ClientError as e:
                logging.error(e)
                return False
    return True


if __name__ == '__main__':
    main()


"""

TODO: implement as new try block; lists all current s3 objects and last date modified
            need resource or client obj sufficient? 

            implementation is below; however nested for loop is inefficient; perhaps append 
            newly uploaded track to empty array and print array at the end using only 1 for loop?

s3_rsrc = boto3.resource('s3')
bucket =  s3.Bucket(bucket_name)

for track in bucket.objects.all():
    print(obj.key, obj.last_modified) 

            # try:
            #     for track in bucket.objects.all():
            #         print(track.key, track.last_modified)
                    
            # except ClientError as e:
            #     logging.error(e)
            #     return False

"""