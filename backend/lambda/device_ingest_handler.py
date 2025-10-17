import json
def lambda_handler(event, context):
    print("Received IoT event:", event)
    return {"statusCode": 200, "body": json.dumps("Ingested successfully")}