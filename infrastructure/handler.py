import json
from application.app import App


def talk(event, context):
    print("-----------E----------")
    print(event)
    print("-----------jsonE----------")
    print(json.dumps(event), indent=4)
    print("------------C---------")

    app = App()

    response = app.talk()

    return response

