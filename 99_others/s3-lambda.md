## s3-lambda-trigger

### what you need

1. Create s3 bucket
2. Create lambda function having a role with "Amazon S3 object read-only permissions" policy template
3. Add trigger of soruce S3 and event type POST
4. Write the code. Make sure to update the `handler` if necessary.
5. Hit deploy
6. Upload a file to your s3 bucket which will trigger the lambda function.
7. go to the monitor tab of your lambda function -> click view cloudwatch logs
8. youll be taken to the log stream of your lamdba function where you'll see the output.

### note:
1. bucket and the lambda has to be in the same region for the trigger to work
2. if file is uploaded via  sdk or aws console then the event type is gonna be PUT
3. optional prefix (folder) or suffix (file extensions) for limiting the trigger notification
4. use different buckets for input and output **to avoid recursion and increased cost**.


### test event
a json object which mocks the structure of the request emitted by AWS services to invoke a lambda