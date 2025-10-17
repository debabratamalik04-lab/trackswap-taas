# TrackSwap — Tracking-as-a-Service (TaaS)

## Overview
TrackSwap offers **Tracking-as-a-Service (TaaS)**, a servitization model for short-term IoT tracking rentals.
Users can rent GPS trackers with refundable deposits, while an **AWS AI Agent** handles telemetry, geofences, anomalies, and automation such as voice calls or notifications.

Built for the **AWS AI Agent Hackathon**, this project demonstrates a scalable IoT + AI ecosystem using AWS.

---

## Architecture
![Architecture](architecture/trackswap_architecture.png)

**AWS Components**
- AWS IoT Core, IoT Device Management
- AWS Lambda, EventBridge, SQS
- Amazon Bedrock (LLM Agent)
- Amazon Location Service (geofencing)
- Amazon Connect (automated calls)
- SNS / Pinpoint (notifications)
- DynamoDB, S3, CloudWatch

---

## Features
- Rent/return IoT trackers (deposit-based model)
- Geofence & route monitoring with AWS Location
- Bedrock AI agent for proactive actions
- Pay-as-you-use billing
- Fleet management & OTA updates

---

## Quick Start
### Prerequisites
- AWS Account with IoT Core, Lambda, Bedrock
- AWS CLI & CDK installed
- Python 3.9+

### Steps
```bash
git clone https://github.com/yourusername/trackswap-taas.git
cd trackswap-taas/backend/cdk
cdk bootstrap
cdk deploy
```
Use `simulator/device_simulator.py` to send test telemetry.

-----
Code sharing is restricted in TCS. We can walk you through the code via screen sharing. 
Please connect with me at my mail id: debabrata.malik@tcs.com


## License
MIT License © 2025 TrackSwap Contributors
