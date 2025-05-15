import boto3

# Initialize EC2 client
ec2_client = boto3.client('ec2')

# Get instances with running state
response = ec2_client.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ]
)

# Print header
print("Running EC2 Instances:")
print("-" * 80)
print(f"{'Instance ID':<20} {'Instance Type':<15} {'Private IP':<15} {'Public IP':<15} {'State':<10}")
print("-" * 80)

# Loop through reservations and instances
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        instance_type = instance['InstanceType']
        private_ip = instance.get('PrivateIpAddress', 'N/A')
        public_ip = instance.get('PublicIpAddress', 'N/A')
        state = instance['State']['Name']
        
        print(f"{instance_id:<20} {instance_type:<15} {private_ip:<15} {public_ip:<15} {state:<10}")