import json
def lambda_handler(event, context):
    print("Triggering Bedrock Agent with event:", event)
    return {"action": "notify_user", "message": "Geofence breach detected!"}