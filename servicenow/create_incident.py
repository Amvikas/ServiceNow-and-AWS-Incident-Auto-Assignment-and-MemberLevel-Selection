import requests
import json

# ServiceNow instance URL
url = "https://nowlearning-nlinst03916202-29uxh-0001.lab.service-now.com/api/now/table/incident"

# credentials
user = "api_user"
pwd = "your_password"

# headers
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# incident data
payload = {
    "short_description": "High CPU detected on EC2 instance",
    "description": "Incident automatically created by Python script",
    "urgency": "2",
    "impact": "2"
}

response = requests.post(
    url,
    auth=(user, pwd),
    headers=headers,
    data=json.dumps(payload)
)

print("Status:", response.status_code)
print(response.json())
