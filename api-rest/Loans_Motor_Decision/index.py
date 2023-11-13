import json
import logging
import boto3
import os

# Crea un cliente DynamoDB
dynamodb = boto3.client('dynamodb', region_name='us-east-1')
lambda_local_client = boto3.client('lambda', region_name='us-east-1')
LOAN_ACCEPTED_PARAM = 300
EMAIL_LAMBDA_NAME = os.environ['LambdaEmailSenderClient']
# Nombre de la tabla en la que deseas insertar datos
CLIENT_SESSION_DYNAMO_TABLE = os.environ['DBTableNewClientsToRegister']


def lambda_response_200():
    return {
        "statusCode": 200,
        "body": "Function executed successfully."
    }


def send_email_first_process(email, first_name, last_name):
    lambda_local_client.invoke(
                FunctionName=EMAIL_LAMBDA_NAME,
                InvocationType='Event',
                Payload=json.dumps(email))


def lambda_handler(event, context):

    for rec in event['Records']:

        if 'OldImage' in rec['dynamodb']:
            payload = rec['OldImage']
            client_id = payload['client_identity_id']['S']
            contact_phone = payload['contact_phone']['S']
            last_name = payload['last_name']['S']
            Id = payload['Id']['S']
            first_name = payload['first_name']['S']
            loan_requested = payload['loan_requested']['S']
            email = payload['email']['S']

            if int(loan_requested) >= LOAN_ACCEPTED_PARAM:
                send_email_first_process(email, first_name, last_name)

    #LOGGER.info('Record: %s', rec)
    return lambda_response_200()
