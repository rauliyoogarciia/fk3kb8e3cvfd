from utils.keyauth.api import Keyauth

keyauthapp = None

def init_keyauth():
    global keyauthapp
    keyauthapp = Keyauth(
        name="FiveChanger",              # Nombre de la app en KeyAuth
        ownerid="hA24nNUgqK",            # Tu Owner ID
        secret="c44bbed31b89300e01b206c7ee201ea8b86ac9d5423ac571b6bcd89e933d80b6",  # App Secret
        version="1.0"
    )
    keyauthapp.init()

def login_user(username, password):
    return keyauthapp.login(username, password)

def register_user(username, password, license_key):
    return keyauthapp.register(username, password, license_key)

def is_authenticated():
    return keyauthapp.check()
