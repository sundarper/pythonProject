import json
import boto3


s3 = boto3.client('s3')
#def lambda_handler(event, context):
def lambda_handler():
    https: // s3 - eu - west - 1.
    amazonaws.com / csparkdata / ol_cdump.json
    bucket = 's3-eu-west-1.amazonaws.com'
    key = '/csparkdata/ol_cdump.json'
    try:
        data = s3.get_object(Bucket=bucket, Key=key)
        json_data = data['Body'].read().decode('utf-8')
        print("first....")
       # print("Content:", json_data)
    except Exception as e:
        raise e

lambda_handler()

