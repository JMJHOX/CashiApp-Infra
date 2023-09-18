import json
import logging
# Configuración de registro
logger = logging.getLogger()
logger.setLevel(logging.INF)


def lambda_handler(event, context):
    logger.info("Hello, World!")
    return {
        "statusCode": 200,
        "body": "Function executed successfully."
    }
