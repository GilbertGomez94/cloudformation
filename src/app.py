import json
import boto3

kinesis = boto3.client('firehose')

def function_handler(event, context):
    body = event["body"]
    body_dict = json.loads(body)
    stream = body_dict["stream"]
    del body_dict["stream"]
    try:
        response = kinesis.put_record(
            DeliveryStreamName=stream,
            Record={
                    'Data': json.dumps(body_dict)
                    })
    except Exception as e:
        response = e
        print(e)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Data on firehose Success",
            "kinesis_response": response
        }),
    }
