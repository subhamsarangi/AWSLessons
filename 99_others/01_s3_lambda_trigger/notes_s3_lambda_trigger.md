## s3-lambda-trigger

### Event JSON of template "s3-put"
```json
{
  "Records": [
    {
      "eventVersion": "2.0",
      "eventSource": "aws:s3",
      "awsRegion": "us-east-1",
      "eventTime": "1970-01-01T00:00:00.000Z",
      "eventName": "ObjectCreated:Put",
      "userIdentity": {
        "principalId": "EXAMPLE"
      },
      "requestParameters": {
        "sourceIPAddress": "127.0.0.1"
      },
      "responseElements": {
        "x-amz-request-id": "EXAMPLE123456789",
        "x-amz-id-2": "EXAMPLE123/5678abcdefghijklambdaisawesome/mnopqrstuvwxyzABCDEFGH"
      },
      "s3": {
        "s3SchemaVersion": "1.0",
        "configurationId": "testConfigRule",
        "bucket": {
          "name": "example-bucket",
          "ownerIdentity": {
            "principalId": "EXAMPLE"
          },
          "arn": "arn:aws:s3:::example-bucket"
        },
        "object": {
          "key": "test%2Fkey",
          "size": 1024,
          "eTag": "0123456789abcdef0123456789abcdef",
          "sequencer": "0A1B2C3D4E5F678901"
        }
      }
    }
  ]
}
```

### what you need

1. Create s3 bucket
2. Create lambda function having a role with "Amazon S3 object read-only permissions" policy template
3. Add trigger of source S3 and event type POST
4. Write the code.
5. Deploy
6. Upload a file to your s3 bucket which will trigger the lambda function.
7. Go to the monitor tab of your lambda function -> click view cloudwatch logs
8. You'll be taken to the log stream of your lamdba function where you'll see the output.

### note:
1. bucket and the lambda has to be in the same region for the trigger to work
2. if file is uploaded via  sdk or aws console then the event type is gonna be PUT
3. optional prefix (folder) or suffix (file extensions) for limiting the trigger notification
4. use different buckets for input and output **to avoid recursion and increased cost**.
5. Make sure to update the `handler` in the code tab if necessary. default handler is `lambda_function.lambda_handler`.


### test event
a json object which mocks the structure of the request emitted by AWS services to invoke a lambda