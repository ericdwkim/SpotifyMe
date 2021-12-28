# NOTE: Populates spotify.audios db table with local audio files using the SQLAlchemy ORM.

import os
import boto3
from dotenv import load_dotenv
import urllib
from src.models import Audio
from src import create_app

# Load environmental variables
load_dotenv()
access_key = os.getenv('access_key')
access_secret = os.getenv('access_secret')
s3_bucket = os.getenv('bucket_name')


def main():

    # Main driver function
    app = create_app()
    app.app_context().push()

    # Connect to S3 service
    s3 = boto3.client(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=access_secret
    )

    def toList(s):
        list_resp = list(s.split(" "))
        return list_resp

    def store_urls(list_url):
        for url in list_url:
            audio = Audio(url)
            audio.insert()

    prefix = "https://s3.us-east-2.amazonaws.com/my.audio.tracks/"
    for k in s3.list_objects(Bucket=s3_bucket)['Contents']:
        list_url_obj = toList(
            prefix + urllib.parse.quote(k['Key'], safe="~()*!.'"))
        store_urls(list_url_obj)


    # TODO: object url requires configuring permissions for each individual s3 object;
    # programmatically access each s3 object; see SAMPLE ACL:
"""
    https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#sample-acl
    https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-policy-keys.html
    https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-arn-format.html
    https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-policy-language-overview.html

"""


if __name__ == '__main__':
    main()
