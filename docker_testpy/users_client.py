import requests


class UsersClient:

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def get_users(self, departament=None):
        if departament:
            resp = requests.get(f"{self.host}:{self.port}/users", {'departament': f"{departament}"})
        else:
            resp = requests.get(f"{self.host}:{self.port}/users")

        return resp.text