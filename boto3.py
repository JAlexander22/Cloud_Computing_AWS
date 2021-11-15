import boto3
from botocore.exceptions import ClientError
import os
import logging

s3 = boto3.resource('s3')

def create_bucket(bucket_name, region='eu-west-1'):
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3' , region_name=region)
            location = {'LocationConstraint':region}
            s3_client.create_bucket(Bucket=bucket_name,CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True

bucketname =input('Bucket Name: ')
create_bucket(bucketname)


def upload_file(file_name,bucket, object_name=None):
    if object_nae is None:
        object_name = os.path.basename(file_name)
    s3_cleint = boto.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
s3 = boto3.client('s3')
with open("test_dir/test.mb", "rb") as f:
    s3.upload_fileobj(f, bucketname, "test.mb")





def delete_bucket():
    ans = input('Do you want to delete bucket? ')
    if ans == "y":
        bucket = s3.Bucket(bucketname)
        bucket.objects.all().delete()
    else:
        print("Bucket not deleted")

delete_bucket(bucketname)
