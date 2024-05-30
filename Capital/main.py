import requests

class capital():
    # SESSION HANDLING
    def __init__(self, token: str=None, email: str=None, password: str=None):
        # HANDLES SESSION AS BASE

        # CHECKS

        if token=="" or token==None: raise ValueError("Token is empty")
        if email=="" or email==None: raise ValueError("Email is empty")
        if password=="" or password==None: raise ValueError("Password is empty")

        # CONSTANTS

        self.APIVersion = "1"
        self.backendURL = "https://api-capital.backend-capital.com/api/v{0}".format(self.APIVersion)
        
        # Request Paramaters

        payload = { "identifier": email, "password": password }
        self.headers = { "X-CAP-API-KEY": token, "Content-Type": "application/json" }

        # Request
        sessionRequest = requests.post(f"{self.backendURL}/session", headers=self.headers, json=payload)

        # Any errors raise them
        if sessionRequest.status_code >= 400: raise ValueError(sessionRequest.json()["errorCode"]) # If capital.com returns error status above 400
        self.accountInfo = sessionRequest.json()

        self.sessionInfo = { "X-SECURITY-TOKEN": sessionRequest.headers.get("X-SECURITY-TOKEN"), "CST": sessionRequest.headers.get("CST") }

    def session(self): # This will get the session information
        sessionDetailsRequest = requests.get(self.backendURL+"/session", headers=self.sessionInfo)
        if sessionDetailsRequest.status_code >= 400: raise ValueError(sessionDetailsRequest.json()["errorCode"]) # If capital.com returns error status above 400

        return sessionDetailsRequest.json()
    
    def switchaccount(self, accountId: str=None): # Will switch the current account on the session
        if accountId=="" or accountId==None: raise ValueError("accountId is empty")
        switchRequest = requests.put(self.backendURL+"/session", headers=self.sessionInfo)

        if switchRequest.status_code >= 400: raise ValueError(switchRequest.json()["errorCode"]) # If capital.com returns error status above 400
        return switchRequest.json()
    
    def destroysession(self): # Destroy the current session you're on
        sessionRequest = requests.delete(self.backendURL+"/session", headers=self.sessionInfo)

        if sessionRequest.status_code >= 400: raise ValueError(sessionRequest.json()["errorCode"]) # If capital.com returns error status above 400
        return sessionRequest.json()
    
    def returnSession(self): # RETURNS ACCOUNT INFORMATION
        return self.sessionInfo

    # SESSION END ENDPOINTS

    # ACCOUNT INFORMATION

    def currency(self): # Return currency information
        return {"type": self.accountInfo["currencyIsoCode"], "symbol": self.accountInfo["currencySymbol"]}
    
    def balance(self, currencySymbol: bool=False): # Return the account balance and the currency symbol at the start depending on True or False
        if currencySymbol: return f'{self.currency()["symbol"]}{self.accountInfo["accountInfo"]["balance"]}'
        else: return f'{self.accountInfo["accountInfo"]["balance"]}'

    def hasdemoaccount(self): # returns bool if there's a demo account
        return f'{self.accountInfo["hasActiveDemoAccounts"]}'
    
    def hasliveaccount(self): # Returns bool on if there's a live account
        return f'{self.accountInfo["hasActiveLiveAccounts"]}'
    
    def clientId(self): # Returns the clientId currently logged in
        return f'{self.accountInfo["clientId"]}'
    
    def available(self, currencySymbol: bool=False): # Returns the available balance of account and currency symbol depending on bool value
        if currencySymbol: return f'{self.accountInfo["accountInfo"]["available"]}{self.accountInfo["accountInfo"]["available"]}'
        else: return f'{self.accountInfo["accountInfo"]["available"]}'

    def accounttype(self): # Returns the type of account.
        return self.accountInfo["accountType"]
    
    # ACCOUNT INFORMATION END


class accounts():
    def __init__(self, sessionInformation=None):
        if sessionInformation == None or sessionInformation == "": ValueError("sessionInformation is empty")

        # CONSTANTS

        self.APIVersion = "1"
        self.backendURL = "https://api-capital.backend-capital.com/api/v{0}".format(self.APIVersion)

        # send a test request to make sure session information is actually correct

        checkRequest = requests.get(self.backendURL+"/accounts", headers=sessionInformation)
        if checkRequest.status_code >= 400: raise ValueError(checkRequest.json()["errorCode"])

        self.headers = sessionInformation # SET HEADERS FOR CLASS
        self.accounts = checkRequest.json()["accounts"] # SAVE THIS INFORMATION FOR IF THEY WANT ACCOUNT INFORMATION

    # END

    def accountsamount(self): # return integer of how many accounts is on your account
        return len(self.accounts)
    
    def returnallaccounts(self): # returns json of all the accounts 
        return self.accounts
    
    def getaccountinfo(self):
        accountPrefRequest = requests.get(self.backendURL+"/accounts/preferences", headers=self.headers)

        if accountPrefRequest.status_code >= 400: raise ValueError(accountPrefRequest.json()["errorCode"])
        
    
