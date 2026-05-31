import json


def get_login_data():

    with open("../Testdata/loginData.json") as f:
        return json.load(f)