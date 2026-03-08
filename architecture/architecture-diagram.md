# Architecture Diagram
This diagram shows the architecture of the **ServiceNow + AWS Self-Healing Incident Automation Platform**.

# System Architecture
Architecture-diagram.png

# Flow Explanation
1. EC2 instance runs the application server.
2. Amazon CloudWatch monitors CPU utilization.
3. If CPU usage exceeds 70%, CloudWatch triggers AWS Lambda.
4. Lambda calls the ServiceNow REST API.
5. ServiceNow automatically creates an incident.
6. Flow Designer triggers automation.
7. The EC2 instance is restarted automatically.
