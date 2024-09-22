import boto3
from botocore.exceptions import NoCredentialsError
s3 = boto3.client('s3')

def upload_file_to_s3(file_name, bucket_name, object_name=None):
    """Upload a file to an S3 bucket.

    :param file_name: File to upload
    :param bucket_name: Target S3 bucket
    :param object_name: S3 object name. If not specified, file_name is used
    :return: True if file was uploaded, else False
    """
    if object_name is None:
        object_name = file_name

    try:
        s3.upload_file(file_name, bucket_name, object_name)
        print(f"File {file_name} uploaded successfully to {bucket_name}/{object_name}")
        return True
    except FileNotFoundError:
        print("The file was not found.")
        return False
    except NoCredentialsError:
        print("Credentials not available.")
        return False

file_name = "example.csv"
bucket_name = "omega-lambda-7-xl-9"
upload_file_to_s3(file_name, bucket_name)
