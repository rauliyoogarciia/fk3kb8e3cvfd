import requests, sys, os
from .checksum import getchecksum

class Keyauth:
    def __init__(self, name, ownerid, secret, version, hash_to_check=None):
        self.name = name
        self.ownerid = ownerid
        self.secret = secret
        self.version = version
        self.hash_to_check = hash_to_check or getchecksum()
        self.baseurl = "https://keyauth.win/api/1.1/"
        self.sessionid = ""
        self.data = None
        self.last_message = ""

    def init(self):
        post_data = {
            "type": "init",
            "ver": self.version,
            "hash": self.hash_to_check,
            "name": self.name,
            "ownerid": self.ownerid,
        }
        self.data = self.req(post_data)

        if not self.data["success"]:
            self.last_message = self.data["message"]
            if self.data["message"] == "invalidver":
                print(f"[!] Versión inválida. Descargando actualización desde: {self.data['download']}")
                os.system(f"start {self.data['download']}")
            else:
                print(f"[!] Error en la inicialización: {self.data['message']}")
            sys.exit()

        self.sessionid = self.data["sessionid"]

    def login(self, username, password):
        post_data = {
            "type": "login",
            "username": username,
            "pass": password,
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid,
        }
        self.data = self.req(post_data)
        self.last_message = self.data.get("message", "")
        return self.data["success"]

    def register(self, username, password, license_key):
        post_data = {
            "type": "register",
            "username": username,
            "pass": password,
            "key": license_key,
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid,
        }
        self.data = self.req(post_data)
        self.last_message = self.data.get("message", "")
        return self.data["success"]

    def check(self):
        post_data = {
            "type": "check",
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid,
        }
        self.data = self.req(post_data)
        self.last_message = self.data.get("message", "")
        return self.data["success"]

    def req(self, data):
        try:
            response = requests.post(self.baseurl, data=data, timeout=10)
            return response.json()
        except Exception as e:
            print(f"[!] Error de conexión: {e}")
            sys.exit()
