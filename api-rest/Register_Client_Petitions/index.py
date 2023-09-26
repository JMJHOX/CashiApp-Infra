import json
import logging
# Configuración de registro
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info("Hello, Probando!")
    return {
        "statusCode": 200,
        "body": "Function executed successfully."
    }
