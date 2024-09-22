def lambda_function(event, context):
    print(context, "---------------->")
    records = event['Records']
    try:
        for record in records:
            print(record['body'])
    except Exception as e:
        print(str(e), "~~~~~~~~~~~~")
    return 1