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

# Architecture Diagram
This project implements a **self-healing cloud infrastructure** by integrating AWS monitoring with ServiceNow incident automation.

![Architecture Diagram](architecture/Architecture-Diagram.png)

# Features
Automatic incident creation
Cloud monitoring integration
Auto-remediation engine
ServiceNow incident updates
