## SQS-lambda

### Event JSON for template 'sqs-receive-message'
```json
{
  "Records": [
    {
      "messageId": "19dd0b57-b21e-4ac1-bd88-01bbb068cb78",
      "receiptHandle": "MessageReceiptHandle",
      "body": "Hello from SQS!",
      "attributes": {
        "ApproximateReceiveCount": "1",
        "SentTimestamp": "1523232000000",
        "SenderId": "123456789012",
        "ApproximateFirstReceiveTimestamp": "1523232000001"
      },
      "messageAttributes": {},
      "md5OfBody": "{{{md5_of_body}}}",
      "eventSource": "aws:sqs",
      "eventSourceARN": "arn:aws:sqs:us-east-1:123456789012:MyQueue",
      "awsRegion": "us-east-1"
    }
  ]
}
```

### what you need
1. Create an SQS queue with default settings, batch size 10, batch window 0
2. Create lambda function having a role with "Amazon SQS poller permissions" policy
3. Add trigger of source SQS
4. Write the code
5. Deploy
6. Send message to Queue
7. Monitor from CloudWatch log streams

### note
1. report batch item failurs allows us to report back the message ids that failed so that only the successfully processed messages can be deleted from the queue and the failed ones get put back on there to be retried.
2. check off 'enable trigger' for testing purpose.