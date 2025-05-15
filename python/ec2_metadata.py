import boto3

# Initialize EC2 client
ec2_client = boto3.client('ec2')

# Get information for specific instance
instance_id = 'i-0c6ccf43e3fe2518d' 

print(f"Retrieving metadata for instance: {instance_id}")

# Get instance details
response = ec2_client.describe_instances(
    InstanceIds=[instance_id]
)

# Extract instance information
instance = response['Reservations'][0]['Instances'][0]

# Display instance metadata
print("\nEC2 Instance Metadata:")
print("-" * 60)
print(f"Instance ID: {instance['InstanceId']}")
print(f"Instance Type: {instance['InstanceType']}")
print(f"Availability Zone: {instance['Placement']['AvailabilityZone']}")
print(f"VPC ID: {instance['VpcId']}")
print(f"Subnet ID: {instance['SubnetId']}")
print(f"State: {instance['State']['Name']}")

# Get network information
if 'PrivateIpAddress' in instance:
    print(f"Private IP: {instance['PrivateIpAddress']}")
if 'PublicIpAddress' in instance:
    print(f"Public IP: {instance['PublicIpAddress']}")

# Get security groups
print("\nSecurity Groups:")
for sg in instance['SecurityGroups']:
    print(f"  {sg['GroupId']} ({sg['GroupName']})")

# Get block device mappings
print("\nBlock Device Mappings:")
for bdm in instance['BlockDeviceMappings']:
    device_name = bdm['DeviceName']
    volume_id = bdm['Ebs']['VolumeId']
    print(f"  {device_name}: {volume_id}")