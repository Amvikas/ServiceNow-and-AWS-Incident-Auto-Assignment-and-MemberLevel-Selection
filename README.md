**ServiceNow AWS Self-Healing Platform**

# Overview
This project demonstrates a cloud incident self-healing system integrating ServiceNow ITSM with AWS monitoring.

When an AWS CloudWatch alarm detects infrastructure issues, Then there will be an automated workflow creates an incident in ServiceNow and attempts to give automated remediation.

# Technologies
ServiceNow
AWS EC2
AWS CloudWatch
AWS Lambda
Python
REST APIs

# Architecture
CloudWatch → Lambda → ServiceNow Incident → Auto Remediation

# Features
Automatic incident creation
Cloud monitoring integration
Auto-remediation engine
ServiceNow incident updates
