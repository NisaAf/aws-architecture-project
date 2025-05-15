# invoke_lambda.py - Invokes a Lambda function with a test event
import boto3
import json

# Initialize Lambda client
lambda_client = boto3.client('lambda')

# Define the Lambda function name
function_name = 's3-upload-logger'

# Create a test event payload
test_event = {
    "Records": [
        {
            "s3": {
                "bucket": {
                    "name": "project-bucket-730335336250"
                },
                "object": {
                    "key": "test-boto3-invoke.txt"
                }
            }
        }
    ]
}

# Invoke Lambda function
print(f"Invoking Lambda function: {function_name}")
response = lambda_client.invoke(
    FunctionName=function_name,
    InvocationType='RequestResponse',
    Payload=json.dumps(test_event)
)

# Process the response
status_code = response['StatusCode']
print(f"Status Code: {status_code}")

# Read and decode the payload
payload = response['Payload'].read().decode('utf-8')
print(f"Response Payload: {payload}")

print("Lambda invocation completed")