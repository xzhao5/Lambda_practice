import boto3
client= boto3.client('ec2')
#ImageID
client.run_instances(ImageID='ami-467ca739',InstanceType='t2.micro', MinCount=1 ,MaxCount1=1)

for instance in resp['Instance']:
    print(instance['IanstanceID'])