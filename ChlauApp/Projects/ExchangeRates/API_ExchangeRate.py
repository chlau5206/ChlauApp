''' API Exchange Rate.py
    Warming: This script contains Access key.  Do not publish to public
    retrive Exchange Rate via API

    pip install requests
    python.exe -m pip install --upgrade pip  

    python version > 3.10

'''

# import requests
import os
import json
import shutil
import urllib3
# from http.client import responses
from datetime import date, datetime
from dotenv import load_dotenv

DEBUG = False
ACCESS_KEY = None        

class ExchangeRateOps():

    def __init__(self):
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
            "400": "The server thinks you made a bad request. This can happen when you do not send along the right data, among other things.",
            "401": "The server thinks you are not authenticated. Many APIs require login ccredentials, so this happens when you do not send the right credentials to access an API.",
            "403": "The resource you are trying to access is forbidden: you do not have the right perlessons to see it.",
            "404": "The resource you tried to access was not found on the server.",
            "503": "The server is not ready to handle the request.",
            }
        
        self.sample_JSON = b'{"success":false,"timestamp":1763580847,"base":"EUR","date":"2025-11-19","rates":{"EUR":1,"USD":1.152538,"CAD":1.620267,"GBP":0.882942,"JPY":180.783096}}'

        ## Replace single quotes with double quotes (JSON standard)
        # self.sample_JSON = self.sample_JSON.replace("'", '"')
        
        # self.file_path = os.getcwd()  # os.path.join( "os.getcwd()", "static", "data" )
        self.project_path = os.path.join(os.curdir, "static", "data")
        self.latest_file = os.path.join(self.project_path, "LatestRate.json")

    ## def format_json(self, json_file):
    #     return json.dumps(json_file, indent = 4)

    def Get_API(self) -> str:
        print ("ExchangeRate Get API ")
        # Create a PoolManager instance
        http = urllib3.PoolManager()
        
        # Make a GET request to the API endpoint
        APIURL = "http://api.exchangeratesapi.io/v1/latest"
        
        try: 
            if DEBUG and os.path.exists(".env.APIkey"):
                load_dotenv(dotenv_path=".env.APIkey")
                print (".env.keys loaded.")
            else:     
                load_dotenv()
                print (".env loaded.")
            ACCESS_KEY = os.getenv("API_KEY")
            
            print (f"Access Key: {ACCESS_KEY}")
            if not ACCESS_KEY :
                raise ValueError("API_KEY not found")
                
        except OSError as e:
            print (f"OSExcept #{e.errno}:{e.strerror} -- {e.filename} ")
        except Exception as e:
            print (f"Error: {e}")
        ######################################################

        exchangeQueryStr = {
            "access_key": ACCESS_KEY,
            "symbols": "EUR,USD,CAD,GBP,JPY,CNY,AUD,HKD,IDR,MXN,SGD,KRW,THB,TWD"
            }
        
        # import urllib3
        rate_data = None
        http_status = {
            # 200: "success",
            400: "unauthorized (missing or invalid API key)",
            403: "forbidden (quota exceeded or not allowed)",
            404: "not found",
            429: "too many requests (rate limit exceeded)"
            # 500+ : "Server error"
            }
        http = urllib3.PoolManager(
            timeout=urllib3.Timeout(connect=2.0, read=5.0),
            retries=urllib3.Retry(total=3, backoff_factor=0.5, status_forcelist=[500, 502, 503, 504])
        )
        response = http.request("GET", APIURL, fields=exchangeQueryStr)
        
        if response.status < 300:   # data in bytes format
            print(f"response code - {response.status}")
            rate_data = response.data
        else: 
            rate_data = self.sample_JSON
            if response.status >= 500:
                print("Server error - try again later.")
            # elif str(response.status) in self.APIStatusCodes.keys:  # status in 400
            #     print(f"API user error: {self.APIStatusCodes[response.status]}")
            else:
                print(f"unknown error: {response.status}")

        return rate_data.decode('utf-8')  # convert to utf-8 string

    def getExchangeRate(self):
        print ("ExchangeRate get rate")
        # for import requests
        # response = requests.get(self.APIURL, params=self.exchangeSymbols) 
        # JSON_data = str()

        today_date = date.today().isoformat()
        todayFile = os.path.join(self.project_path, "ExchangeRate_" + today_date + ".json")
        # if exchange rate loaded today, then skip Get_API, read latestfile instead.
        # if os.path.exists(todayFile):
        #     print ("Exchange rate file exist.")
        # else:
        JSON_data = self.Get_API()
        if DEBUG:
            JSON_Print(JSON_data)
        try:
            with open(todayFile, 'w') as writeFile:
                writeFile.write(JSON_data)
                writeFile.close()
            with open(self.latest_file, 'w') as LatestFile:
                LatestFile.write(JSON_data)
                LatestFile.close()

        except IOError as e: 
            st = None
            if not os.path.exists(os.path.dirname(self.file_path)): 
                st = f"{e}.  The directory does not exist."
            elif not os.access(os.path.dirname(self.file_path), os.W_OK): 
                st = f"{e}.  You do not have write permissions to {self.file_path}."
            elif os.path.isfile(todayFile) and not os.access(todayFile, os.W_OK):
                st = f"{e}.  You do not have write permissions to {todayFile}."
            elif os.path.isfile(self.latest_file) and not os.access(self.latest_file, os.W_OK):
                st = f"{e}.  You do not have write permissions to {self.latest_file}."
            print(st)
        except ValueError as e:
            print(f"Incorrect value. {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
        return True

    def copy_latest_file(self):
        print ("ExchangeRate copy latest file")
        try: 
            source = self.latest_file
            destination = "/home/chlau5206/ChlauApp/ChlauApp/Projects/ExchangeRates/static/data/LatestRate.json"
            shutil.copy(source, destination)
            print(f"File copied to {destination}.")
        except Exception as e: 
            print(f'Error: {e}')

def JSON_Print(obj):
#     # format_json = lambda json_file : json.dumps(json_file, indent = 4)
#     # parsed = json.loads(obj)
#     # formatted = json.dumps(parsed, sort_keys=True, indent=4)
#     # print(formatted)
    print(json.dumps(json.loads(obj), sort_keys=True, indent=4))

if __name__=="__main__":
    EX = ExchangeRateOps()
    response = EX.getExchangeRate()
    # EX.copy_latest_file()
    
    
