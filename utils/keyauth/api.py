import requests, json, hashlib, time, os, sys
from .checksum import getchecksum

class Keyauth:
    def __init__(self, name, ownerid, secret, version, hash_to_check=None):
        self.name = name
        self.ownerid = ownerid
        self.secret = secret
        self.version = version
        self.hash_to_check = hash_to_check
        self.baseurl = "https://keyauth.win/api/1.1/"
        self.sessionid = ""
        self.encKey = None
        self.data = None

    def init(self):
        if self.hash_to_check is None:
            self.hash_to_check = getchecksum()

        post_data = {
            "type": "init",
            "ver": self.version,
            "hash": self.hash_to_check,
            "name": self.name,
            "ownerid": self.ownerid,
        }
        self.data = self.req(post_data)

        if not self.data["success"]:
            if self.data["message"] == "invalidver":
                print(f"[!] Versión inválida. Descargando actualización desde: {self.data['download']}")
                os.system(f"start {self.data['download']}")
                sys.exit()
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
        return self.data["success"], self.data.get("message", "Error desconocido")

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
        return self.data["success"], self.data.get("message", "Error desconocido")

    def check(self):
        post_data = {
            "type": "check",
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid,
        }
        self.data = self.req(post_data)
        return self.data["success"]

    def req(self, data):
        try:
            response = requests.post(self.baseurl, data=data, timeout=10)
            return response.json()
        except Exception as e:
            print(f"[!] Error de conexión: {e}")
            sys.exit()
