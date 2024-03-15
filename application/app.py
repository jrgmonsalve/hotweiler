import json


class App:
    def __init__(self):
        pass

    def talk(self):

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Hello World!"
            }),
        }