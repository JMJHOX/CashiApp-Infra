import json
import logging
import boto3
import os

ses_local_client = boto3.client('ses', region_name='us-east-1')
# Nombre de la tabla en la que deseas insertar datos
CLIENT_SESSION_DYNAMO_TABLE = os.environ['DBTableNewClientsToRegister']
SOURCE_EMAIL_SENDER = os.environ['SourceEmailSender']



def send_email(email_client):
    
    response = ses_local_client.send_email(
    Destination={
        'ToAddresses': email_client
    },
    Message={
        'Body': {
            'Text': {
                'Charset': 'UTF-8',
                'Data': 'This is the message body in text format.',
            }
        },
        'Subject': {
            'Charset': 'UTF-8',
            'Data': 'Test email',
        },
    },
    Source=SOURCE_EMAIL_SENDER
    )
    
    print(response)
    
    return {
        'statusCode': 200,
        'body': json.dumps("Email Sent Successfully. MessageId is: " + response['MessageId'])
    }


def lambda_handler(event, context):
    email_client = event['email']
    print("h")
    return send_email(email_client)
