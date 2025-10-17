def lambda_handler(event, context):
    print("Calculating usage and billing...")
    return {"status": "success", "billing": 2.99, "currency": "USD"}