# Demo Video

This video demonstrates the complete workflow of the project:

- AWS CloudWatch monitoring
- Lambda triggering
- ServiceNow incident creation
- Auto assignment to team/member

## Watch Demo

[![Watch Demo](https://img.youtube.com/vi/h7dNFtdxOXw/0.jpg)](https://youtu.be/h7dNFtdxOXw)

# Description

This project integrates AWS cloud monitoring with ServiceNow ITSM to automate the full incident assignment pipeline. When Amazon CloudWatch detects high CPU utilization on an EC2 instance, AWS Lambda triggers the ServiceNow REST API to create an incident, which is then automatically assigned to the Cloud Operations group and a specific team member using dynamic selection logic (Round-Robin, On-Call Schedule, or Availability Check).
