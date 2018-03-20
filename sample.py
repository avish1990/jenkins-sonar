import boto3
import time
import json
import sys

def handler(event, context):

    ssm = boto3.client('ssm')
    message = event['Records'][0]['Sns']['Message']
    documentName = 'AWS-RunShellScript'
    commandopen = ['iptables -I INPUT -p tcp --dport 8080 -j ACCEPT']
    commandclose  = ['iptables -I INPUT -p tcp --dport 8080 -j DROP']
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    for r in response['Reservations']:
      for instance in r['Instances']:
        instanceid = instance['InstanceId']
        if message.lower() == 'start':
          status = ssm.send_command(DocumentName=documentName, Parameters={'commands': commandopen}, InstanceIds=[instanceid])
        elif message.lower() == 'stop':
          status = ssm.send_command(DocumentName=documentName, Parameters={'commands': commandclose}, InstanceIds=[instanceid])
        else:
          print('Invalid Input')
