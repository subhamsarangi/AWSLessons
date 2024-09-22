import csv
import io
import boto3

s3_client = boto3.client('s3')

def lambda_function(event, context):
    s3_record = event['Records'][0]['s3']
    bucket = s3_record['bucket']['name']
    key = s3_record['object']['key']
    print(bucket, '\n', key)

    response = s3_client.get_object(Bucket=bucket, Key=key)

    data = response['Body'].read().decode('utf-8')
    reader = csv.reader(io.StringIO(data))
    next(reader) # skip header
    # csv header: id,first_name,last_name,email,gender,ip_address
    for row in reader:
        try:
            print(f'email {row[3]}, ip_address {row[5]}')
        except:
            print(str(row))
    return 1