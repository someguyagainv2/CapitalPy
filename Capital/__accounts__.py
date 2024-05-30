import requests
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

    def amount(self): # return integer of how many accounts is on your account
        return len(self.accounts)
    
    def returnall(self): # returns json of all the accounts 
        return self.accounts
    
    def getinfo(self): # Returns json information on all the account paramaters
        accountPrefRequest = requests.get(self.backendURL+"/accounts/preferences", headers=self.headers)

        if accountPrefRequest.status_code >= 400: raise ValueError(accountPrefRequest.json()["errorCode"])
        return accountPrefRequest.json()
    
    def leverages(self): # return all leverages related information
        accountPrefRequest = requests.get(self.backendURL+"/accounts/preferences", headers=self.headers)

        if accountPrefRequest.status_code >= 400: raise ValueError(accountPrefRequest.json()["errorCode"])
        return accountPrefRequest.json()["leverages"]
    
    # leverages information
    
    def getshares(self): # return all shares information 
        accountPrefRequest = requests.get(self.backendURL+"/accounts/preferences", headers=self.headers)

        if accountPrefRequest.status_code >= 400: raise ValueError(accountPrefRequest.json()["errorCode"])
        return accountPrefRequest.json()["leverages"]["SHARES"]
    
    def getcurrencies(self): # return all currencies information 
        accountPrefRequest = requests.get(self.backendURL+"/accounts/preferences", headers=self.headers)

        if accountPrefRequest.status_code >= 400: raise ValueError(accountPrefRequest.json()["errorCode"])
        return accountPrefRequest.json()["leverages"]["CURRENCIES"]

    def getindices(self): # return all indices information 
        accountPrefRequest = requests.get(self.backendURL+"/accounts/preferences", headers=self.headers)

        if accountPrefRequest.status_code >= 400: raise ValueError(accountPrefRequest.json()["errorCode"])
        return accountPrefRequest.json()["leverages"]["INDICES"]
    
    def getcrypto(self): # return all cryptocurrencies information 
        accountPrefRequest = requests.get(self.backendURL+"/accounts/preferences", headers=self.headers)

        if accountPrefRequest.status_code >= 400: raise ValueError(accountPrefRequest.json()["errorCode"])
        return accountPrefRequest.json()["leverages"]["CRYPTOCURRENCIES"]
    
    def getcommodities(self): # return all commodities information 
        accountPrefRequest = requests.get(self.backendURL+"/accounts/preferences", headers=self.headers)

        if accountPrefRequest.status_code >= 400: raise ValueError(accountPrefRequest.json()["errorCode"])
        return accountPrefRequest.json()["leverages"]["COMMODITIES"]
    
    # LEVERAGES INFORMATION END

    def update(self, newPreferences=None): # Update preferences on capital account
        if newPreferences == None or newPreferences=="": raise ValueError("newPreferences is empty")

        updateAccountRequest = requests.put(self.backendURL+"/accounts/preferences", headers=self.headers, json=newPreferences)
        if updateAccountRequest.status_code >= 400: raise ValueError(updateAccountRequest.json()["errorCode"])
        return updateAccountRequest.json()["leverages"]["COMMODITIES"]
    
    def updatedemo(self, amount: int=1000): # Update the demo account balance to new value
        updateDemoRequest = requests.put(self.backendURL+"/accounts/topUp", headers=self.headers)
        if updateDemoRequest.status_code >= 400: raise ValueError(updateDemoRequest.json()["errorCode"])
        return updateDemoRequest.json()["successful"]