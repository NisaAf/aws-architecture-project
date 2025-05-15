import boto3
import uuid

# Initialize S3 client
s3_client = boto3.client('s3')

# Create a unique bucket name
bucket_name = f"boto3-bucket-{uuid.uuid4().hex[:8]}"
print(f"Creating bucket: {bucket_name}")

# Create the bucket
s3_client.create_bucket(Bucket=bucket_name)
print(f"Bucket created successfully: {bucket_name}")

# Create a file to upload
file_name = 'boto3-test-file.txt'
with open(file_name, 'w') as f:
    f.write('This file was created and uploaded using Boto3')
print(f"Created file: {file_name}")

# Upload the file
s3_client.upload_file(file_name, bucket_name, file_name)
print(f"File {file_name} uploaded to {bucket_name}")

print("S3 operations completed successfully")