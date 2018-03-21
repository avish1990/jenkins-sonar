import boto3

def handler(event, context):
    ssm = boto3.client('ssm')
    message = event['Records'][0]['Sns']['Message']
    documentName = 'avish-port'
    response=ssm.send_command(DocumentName=documentName,  Parameters={'Rule': [message.upper()]},  Targets=[{'Key': 'tag:env','Values': ['dev']}])
