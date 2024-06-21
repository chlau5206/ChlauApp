''' API Exchange Rate.py
    retrive Exchange Rate via API

    pip install requests
    python.exe -m pip install --upgrade pip  

    python version > 3.10

    
    /home/chlau5206/ProjectA/app/static/app/API_ExchangeRage.py
'''

# import requests
import os
import sys
import urllib3
import json
import datetime 
from datetime import date

class ExchangeRateOps():
    def __init__(self):
        self.APIURL = "http://api.exchangeratesapi.io/v1/latest"
        self.exchangeQueryStr = {
            "access_key":"55eb6ba3d802fe4293295db452a16a9f",
            "symbols":"EUR,USD,CAD,GBP,JPY,CNY,AUD,HKD,IDR,MXN,SGD,KRW,THB,TWD"\
            }
        self.symbols = {
            "CAD":"CANADIAN DOLLAR",
            "GBP":"BRITISH POUND",
            "EUR":"EURO",
            "JPY":"JAPANESE YEN",
            "CNY":"CHINESE YUAN",
            "AUD":"AUSTRALIAN DOLLAR",
            "HKD":"HONG KONG DOLLAR",
            "IDR":"INDONESIAN RUPIAH",
            "MXN":"MEXICAN PESO",
            "SGD":"SINGAPORE DOLLAR",
            "KRW":"SOUTH KOREAN WON",
            "THB":"THAI BAHT",
            "TWD":"NEW TAIWAN DOLLAR",
            "USD":"US DOLLAR",
            }

        self.APIStatusCodes = {
            "200": "Everything went okay, and the result has been returned (if any).",
            "301": "The server is redirecting you to a different endpoint. This can happen when a company switches domain names, or an endpoint name is changed.",
            "400": "The server thinks you made a bad request. This can happen when you don’t send along the right data, among other things.",
            "401": "The server thinks you’re not authenticated. Many APIs require login ccredentials, so this happens when you don’t send the right credentials to access an API.",
            "403": "The resource you’re trying to access is forbidden: you don’t have the right perlessons to see it.",
            "404": "The resource you tried to access wasn’t found on the server.",
            "503": "The server is not ready to handle the request.",
            }
        
        # self.filePath = r'~/ProjectA/app/Data'
        # self.filePath = r'/home/chlau5206/ProjectA/app/Data'
        #self.filePath = r'F:\.src\DjangoSolutions\ProjectA\app\Data'
        self.filePath = r"D:\Python\Projects\Project2\chlauApp\static\data.json"

    def getSample(self) -> None:
        rateFile = os.path.join(self.filePath, "LastRate.json")
        data = b'{"success":true,"timestamp":1712252526,"base":"EUR","date":"2024-sample","rates":{"EUR":1,"USD":1.086131,"MXN":17.932246,"SGD":1.462384,"KRW":1460.499318,"THB":39.817943,"TWD":34.789331}}'
        
        if os.path.isfile(rateFile):
            with open(rateFile, 'wb') as writeFile:
                writeFile.write(data)
        else: 
            print ("Error: sample file not found.")

        return 

    def getAPI(self) -> None:
        ## import urllib3
        http = urllib3.PoolManager()
        response = http.request("GET", 
                                self.APIURL,
                                fields=self.exchangeQueryStr )
        today = date.today().isoformat()
        currentTime = datetime.datetime.now().isoformat()
        if response.status == 200:
            rateFile = os.path.join(self.filePath, "ExchangeRate" + today + ".json")
            lastRateFile = os.path.join(self.filePath, "LastRate.json")
            with open(rateFile, 'wb') as writeFile:
                writeFile.write(response.data)
            with open(lastRateFile, 'wb') as writeFile:
                writeFile.write(response.data)
        else:
            errorLog = os.path.join(self.filePath, "API_ExchangeRateError.log")
            errorStr = f"{currentTime}:Error[" + str({response.status}) + "] " + EX.APIStatusCodes[response.status]
            with open("API_ExchangeRate_Error.log", 'a') as appendFile:
                appendFile.write(errorStr)
            
                    
    def getExchangeRate(self) -> dict:
        ## for import requests
        # response = requests.get(self.APIURL, params=self.exchangeSymbols) 

        today = date.today().isoformat()
        rateFile = os.path.join(self.filePath, "ExchangeRate" + today + ".json")
        rateJSON = {}
        if not os.path.isfile(rateFile):
            rateFile = os.path.join(self.filePath, "LastRate.json")
        with open(rateFile, "r") as readFile:
            rateJSON = json.load(readFile)
            
        return rateJSON

    def jsonPrint(self, obj):
        # create a formatted string of the Python JSON object
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)

        # jprint(response.json())

if __name__=="__main__":
    EX = ExchangeRateOps()
    # EX.jsonPrint(EX.getAPI())
    EX.jsonPrint(EX.getSample())

    response = EX.getExchangeRate()
    EX.jsonPrint(response)
    