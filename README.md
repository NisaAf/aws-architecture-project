# AWS Architecture Project

This project implements a scalable AWS architecture using Infrastructure as Code (IaC).

## Project Overview

The architecture includes:
- VPC with public and private subnets
- EC2 instances behind an Application Load Balancer
- Auto Scaling for the web server layer
- RDS database
- S3 bucket for file storage
- Lambda function for S3 upload monitoring
- CloudFormation and Terraform for infrastructure deployment

## Repository Structure

- `/terraform`: Terraform scripts for networking components
- `/cloudformation`: CloudFormation templates for resource deployment
- `/python`: Python scripts using Boto3 to interact with AWS
- `/lambda`: Lambda function code
- `/docs`: Project documentation and architecture diagram
