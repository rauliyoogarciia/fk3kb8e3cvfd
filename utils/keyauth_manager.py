from utils.keyauth.api import Keyauth

keyauthapp = None

def init_keyauth():
    global keyauthapp
    keyauthapp = Keyauth(
        name="FiveChanger",             # Nombre en tu panel de KeyAuth
        ownerid="hA24nNUgqK",          # Sustituye por tu Owner ID
        secret="c44bbed31b89300e01b206c7ee201ea8b86ac9d5423ac571b6bcd89e933d80b6",  # Sustituye por tu App Secret
        version="1.0"
    )
    keyauthapp.init()

def login_user(username, password):
    success, message = keyauthapp.login(username, password)
    print(f"Login success: {success}, message: {message}")
    return success

def register_user(username, password, license_key):
    success, message = keyauthapp.register(username, password, license_key)
    print(f"Registro success: {success}, message: {message}")
    return success, message

def is_authenticated():
    return keyauthapp.check()
