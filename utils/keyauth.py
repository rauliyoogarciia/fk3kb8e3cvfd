import requests
import hashlib
import sys
import json

class Keyauth:
    def __init__(self, name, ownerid, version, hash_to_check):
        self.name = name
        self.ownerid = ownerid
        self.version = version
        self.hash = hash_to_check
        self.sessionid = None
        self.data = None
        self.baseurl = "https://keyauth.win/api/1.1/"

    def _post(self, type, post_data):
        post_data.update({
            "type": type,
            "name": self.name,
            "ownerid": self.ownerid
        })
        response = requests.post(self.baseurl, data=post_data)
        result = response.json()

        if result.get("success"):
            self.sessionid = result.get("sessionid", None)
            self.data = result
        else:
            raise Exception(result.get("message", "Error desconocido."))

    def login(self, username, password):
        self._post("login", {
            "username": username,
            "pass": password,
        })

    def register(self, username, password, license_key):
        self._post("register", {
            "username": username,
            "pass": password,
            "key": license_key
        })
