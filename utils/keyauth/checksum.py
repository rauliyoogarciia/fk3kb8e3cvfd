import hashlib

def getchecksum():
    with open(__file__, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()
