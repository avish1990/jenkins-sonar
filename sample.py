import boto3
import time
import json
import sys

def lambda_handler(event, context):

    ssm = boto3.client('ssm')
    message = event['Records'][0]['Sns']['Message']
    documentName = 'AWS-RunShellScript'
    commandopen = ['iptables -I INPUT -p tcp --dport 8080 -j ACCEPT']
    commandclose  = ['iptables -I INPUT -p tcp --dport 8080 -j DROP']
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    for r in response['Reservations']:
      for instance in r['Instances']:  
	
        if message.lower() == 'start':
          status = ssm.send_command(DocumentName=documentName, TimeoutSeconds=timeout, Parameters={'commands': commandopen}, InstanceIds=[instance])
        elif message.lower() == 'stop':
          status = ssm.send_command(DocumentName=documentName, TimeoutSeconds=timeout, Parameters={'commands': commandclose}, InstanceIds=[instance])
        else:
          print('Invalid Input')
