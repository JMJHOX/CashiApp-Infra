import json
import logging
import boto3
import os

# Crea un cliente DynamoDB
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

# Nombre de la tabla en la que deseas insertar datos
CLIENT_SESSION_DYNAMO_TABLE = os.environ['DBTableNewClientsToRegister']


def lambda_response_200():
    return {
        "statusCode": 200,
        "body": "Function executed successfully."
    }


def register_client_on_dynamo(uuid, payload):
    # Datos que deseas insertar
    item = {
        'Id': {'S': uuid},  # Un atributo numérico
        'first_name': {'S': payload['first_name']},  # Un atributo de cadena
        'last_name': {'S': payload['last_name']},  # Otro atributo numérico
        # Otro atributo numérico
        'client_identity_id': {'S': payload['client_identity_id']},
        'email': {'S': payload['email']},  # Otro atributo numérico
        # Otro atributo numérico
        'contact_phone': {'S': payload['contact_phone']},
        'loan_requested': {'S': payload['loan_qty']},  # Otro atributo numérico
    }

    # Inserta el elemento en la tabla
    response = dynamodb.put_item(
        TableName=CLIENT_SESSION_DYNAMO_TABLE, Item=item)
    print(response)


def lambda_handler(event, context):
    payload = event['payload']
    request_id = context.aws_request_id
    register_client_on_dynamo(request_id, payload)
    return lambda_response_200()
