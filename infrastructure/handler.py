import json
from application.app import App


def ask(event, context):
    print("-----------E----------")
    print(event)
    print("-----------jsonE----------")
    print(json.dumps(event), indent=4)
    print("------------C---------")
    print(context)
    print("------------jsonC---------")
    print(json.dumps(context), indent=4)
    print("-------------Fin--------")
    app = App()

    response = app.ask()

    return response

