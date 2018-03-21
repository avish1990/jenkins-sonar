import boto3

def handler(event, context):
    ssm = boto3.client('ssm')
    message = event['Records'][0]['Sns']['Message']
    Doc = 'avish-port'
    response=ssm.send_command(DocumentName=Doc,  Parameters={'Rule': [message.upper()]},  Targets=[{'Key': 'tag:env','Values': ['dev']}])
