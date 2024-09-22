import os
import boto3
from botocore.exceptions import NoCredentialsError, ClientError
from dotenv import load_dotenv

load_dotenv()

sqs = boto3.client('sqs')

queue_name = os.getenv('SQS_QUEUE_NAME')
message_body = "Boricua (ha), morena (ha), dominicano (ha), colombiano (ha)"

def send_message_to_sqs(queue_name, message_body):
    """Send a message to an SQS queue using the queue name.

    :param queue_name: Name of the SQS queue
    :param message_body: The content of the message to send
    :return: True if the message was sent successfully, else False
    """
    try:
        account_region = os.getenv('AWS_REGION')
        account_id = os.getenv('AWS_ACCOUNT_ID')
        queue_url = f"https://sqs.{account_region}.amazonaws.com/{account_id}/{queue_name}"
        # queue_url = sqs.get_queue_url(QueueName=queue_name)['QueueUrl']

        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=message_body
        )
        print(f"Message sent successfully. Message ID: {response['MessageId']}")
        return True
    except NoCredentialsError:
        print("Credentials not available.")
        return False
    except ClientError as e:
        print(f"Failed to send message: {e}")
        return False

send_message_to_sqs(queue_name, message_body)
