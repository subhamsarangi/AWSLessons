import os
import random
import string
import boto3
from botocore.exceptions import NoCredentialsError
from slugify import slugify
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client('s3')
bucket_name = os.getenv('S3_BUCKET_NAME')

file_name = "01_s3_lambda_trigger/my example.csv"

def generate_random_string(length=8):
    """Generate a random string of fixed length."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def upload_file_to_s3(file_name, bucket_name, object_name=None):
    """Upload a file to an S3 bucket.

    :param file_name: File to upload
    :param bucket_name: Target S3 bucket
    :param object_name: S3 object name. If not specified, file_name is used
    :return: True if file was uploaded, else False
    """

    if object_name is None:
        random_string = generate_random_string()
        base_name = os.path.basename(file_name)
        base_name, ext = os.path.splitext(os.path.basename(file_name))
        object_name = f"{slugify(base_name)}_{random_string}{ext}"

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

upload_file_to_s3(file_name, bucket_name)
