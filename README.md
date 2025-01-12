# Cloud-Computing-Elastic-Face-Recognition-Web-App-with-AWS-IaaS
Builds an elastic application using AWS IaaS, automating resource management with EC2, Elastic IP, and Python. Develops a web tier for concurrent face recognition requests, emulating model inference. Includes testing with a workload generator and delivers high scalability. Ensures accurate results under varying loads.

Step 1: AWS Development Setup
Create an AWS Account:
Use the "Personal" account type, provide contact and payment details, and select the Basic Plan.
Obtain AWS Access Keys:
Generate Access Key ID and Secret Access Key from the AWS Management Console under Security Credentials.

Set Up IAM Users:
Create two IAM users:
Development IAM: Full permissions for project-related tasks.
Grading IAM: Limited permissions (AmazonEC2ReadOnlyAccess) for evaluation.

Install and Configure AWS CLI:
Install AWS CLI as per the documentation for your OS.
Configure CLI using the command aws configure by providing your access keys, default region (e.g., us-east-1), and output format (e.g., JSON).

Step 2: EC2 Instance Setup
Set Security Credentials:
Create a key pair in the EC2 dashboard and save the PEM file securely.
Add SSH inbound rules for secure instance access.
Launch EC2 Instance:
Use AMI ami-0a0e5d9c7acc336f1 (Ubuntu 22.04, t2.micro) for resource creation.
Configure tags and start the instance.
Assign Elastic IP:
Allocate a static Elastic IP and associate it with the EC2 instance to ensure consistent access during testing.

Step 3: Develop Web Tier
Implement Face Recognition Lookup:
Design the web tier to handle HTTP POST requests at the root endpoint (/) with the payload key inputFile for image uploads.
Use a lookup table to emulate face recognition model inference and return predictions in <filename>:<prediction_result> format.
Handle Concurrent Requests:
Ensure the web tier processes multiple requests concurrently.
Test performance with the provided workload generator:
Expected runtime for 1000 concurrent requests: ~13.67 seconds.
Expected runtime for 100 concurrent requests: ~2.04 seconds.
