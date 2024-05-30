import requests

class capital():
    def __init__(self, token: str=None, email: str=None, password: str=None):
        if token=="" or token==None: raise ValueError("Token is empty")
        if email=="" or email==None: raise ValueError("Email is empty")
        if password=="" or password==None: raise ValueError("Password is empty")




service = capital("")
