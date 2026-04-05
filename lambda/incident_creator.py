import json
import urllib3
import base64

http = urllib3.PoolManager()

SERVICENOW_URL = "https://nowlearning-nlinst03916202-29uxh-0001.lab.service-now.com/api/now/table/incident"
USERNAME = "api_user"
PASSWORD = "Vikas@123"

def lambda_handler(event, context):

    payload = {
        "short_description": "AWS CloudWatch High CPU Alert",
        "description": "CloudWatch detected high CPU usage on EC2 instance",
        "urgency": "2",
        "impact": "2"
    }

    auth_string = f"{USERNAME}:{PASSWORD}"
    encoded_auth = base64.b64encode(auth_string.encode()).decode()

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {encoded_auth}"
    }

    response = http.request(
        "POST",
        SERVICENOW_URL,
        body=json.dumps(payload),
        headers=headers
    )

    print(response.data)

    return {
        "statusCode": response.status,
        "body": response.data.decode("utf-8")
    }
