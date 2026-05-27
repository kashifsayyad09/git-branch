import boto3

# Create EC2 client
ec2 = boto3.client('rds', region_name='ap-south-1')

# Launch EC2 Instance
response = ec2.run_instances(
    ImageId='ami-0f58b397bc5c1f2e8',   # Amazon Linux 2023 AMI
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    KeyName='your-keypair-name',
    SecurityGroupIds=['sg-xxxxxxxx'],
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Python-EC2-Instance'
                }
            ]
        }
    ]
)

print("EC2 Instance Created Successfully!")
print("Instance ID:", response['Instances'][0]['InstanceId'])
