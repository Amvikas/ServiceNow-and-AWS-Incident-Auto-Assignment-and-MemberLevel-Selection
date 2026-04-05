# ServiceNow + AWS Incident Auto Assignment and Member-Level Selection

> Automatically creates and assigns ServiceNow incidents to the right team member when AWS CloudWatch detects infrastructure issues — no manual triage required.

## Overview

This project integrates **AWS cloud monitoring** with **ServiceNow ITSM** to automate the full incident assignment pipeline. When Amazon CloudWatch detects high CPU utilization on an EC2 instance, AWS Lambda triggers the ServiceNow REST API to create an incident, which is then automatically assigned to the **Cloud Operations** group and a specific team member using dynamic selection logic (Round-Robin, On-Call Schedule, or Availability Check).

## Architecture

![Architecture Diagram](architecture/serviceNow_AWS.png)

This project started as a way to solve a real problem I kept running into — whenever an AWS EC2 instance spiked in CPU usage, someone had to manually check CloudWatch, figure out what happened, create a ticket in ServiceNow, and then assign it to the right person on the Cloud Operations team. That whole process was slow and error-prone, especially when it happened outside business hours.
So I built a small integration that handles all of that automatically. When CloudWatch detects CPU utilization crossing 70%, it triggers a Lambda function that hits the ServiceNow REST API and creates an incident on its own. From there, a Business Rule inside ServiceNow takes over — it checks whether the incident came from AWS, sets the assignment group to Cloud Operations, and then picks a specific team member to assign it to using a round-robin approach across the active members of that group.
The result is that by the time anyone opens ServiceNow, the incident is already created, already assigned to someone, and ready to be worked. No manual triage, no wondering who should pick it up.
I also wrote a small Python script to test the API integration independently, which helped a lot during development for verifying that the incident creation was working before hooking up the full Lambda pipeline.

