import json


def logger(function):
    def get_output(*args):
        response = function(*args)
        print(response)
        return response
    return get_output


@logger
def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "title": "Test Item",
            "price": 159.89,
            "quantity": 12
        }),
    }


