from xmlrpc.client import ResponseError
import boto3
import json

client = boto3.client('resourcegroupstaggingapi', region_name='us-east-2')

tags = client.get_resources(ResourceTypeFilters=['ec2:instance'])

print(tags)

print(json.dumps(tags, indent=4))