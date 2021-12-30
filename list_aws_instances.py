import boto3

client = boto3.client('ec2',
    aws_access_key_id="YOUR_KEY",
    aws_secret_access_key="YOUR_SECRET_KEY",
    region_name="us-east-2"
)

response = client.describe_instances()

publicIp = []
keyName = []

for j in range(len(response['Reservations'])):
    for i in response['Reservations'][j]['Instances']:
        temp_dict = { items[0]: i.get('PublicIpAddress'), items[1]: i.get('KeyName') }
        publicIp.append(i.get('PublicIpAddress'))
        keyName.append(i.get('KeyName'))


print(publicIp)
print(keyName)
