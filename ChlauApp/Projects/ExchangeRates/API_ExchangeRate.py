''' API Exchange Rate.py
'''

# import requests
import os
import json
import shutil
import urllib3
# from http.client import responses
import requests 
from datetime import date, datetime
from dotenv import load_dotenv

DEBUG = True

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
            "101":  "No API Key was specified or an invalid API Key was specified.",
            "102":  "The account this API request is coming from is inactive.",
            "103":  "The requested API endpoint does not exist.",
            "104":  "The maximum allowed API amount of monthly API requests has been reached.",
            "105":	"The current subscription plan does not support this API endpoint.",
            "106":	"The current request did not return any results.",
            
            "200": "Everything went okay, and the result has been returned (if any).",
            "201":	"An invalid base currency has been entered.",
            "202":	"One or more invalid symbols have been specified.",
            
            "301":	"No date has been specified. [historical]",
            "302":	"An invalid date has been specified. [historical, convert]",

            "400": "The server thinks you made a bad request. This can happen when you do not send along the right data, among other things.",
            "401": "The server thinks you are not authenticated. Many APIs require login ccredentials, so this happens when you do not send the right credentials to access an API.",
            "403":	"No or an invalid amount has been specified. [convert]",
            "404":	"The requested resource does not exist.",
            
            "501":	"No or an invalid timeframe has been specified. [timeseries]",
            "502": 	"No or an invalid 'start_date' has been specified. [timeseries, fluctuation]",
            "503":	"No or an invalid 'end_date' has been specified. [timeseries, fluctuation]",
            "504":	"An invalid timeframe has been specified. [timeseries, fluctuation]",
            "505":	"The specified timeframe is too long, exceeding 365 days. [timeseries, fluctuation]"
        }

        self.sample_JSON = b'{"success":false,"timestamp":1763580847,"base":"EUR","date":"2025-11-19","rates":{"EUR":1,"USD":1.152538,"CAD":1.620267,"GBP":0.882942,"JPY":180.783096}}'

        ## Replace single quotes with double quotes (JSON standard)
        # self.sample_JSON = self.sample_JSON.replace("'", '"')
        
        self.project_path = os.path.join(os.curdir, "static", "data")
        self.latest_file = os.path.join(self.project_path, "LatestRate.json")

    def get_AccesKey(self) -> str:
        print ('Get Access Key')
        #key = ""
        print (f"Where: {os.getcwd()}")
        try: 
            if DEBUG and os.path.exists(".env.APIkey"):
                load_dotenv(dotenv_path=".env.APIkey")
                print (".env.keys loaded.")
            else:     
                load_dotenv()
                print (".env loaded.")
            key = os.getenv("API_KEY")
            
            if not key :
                raise ValueError("API_KEY not found")
                
        except OSError as e:
            print (f"OSExcept #{e.errno}:{e.strerror} -- {e.filename} ")
        except Exception as e:
            print (f"Error: {e}")
        
        return key

    def get_API_urlLib3(self) -> str:
        print ("ExchangeRate Get API ")
        # Create a PoolManager instance
        http = urllib3.PoolManager()
        # Make a GET request to the API endpoint
        APIURL = "http://api.exchangeratesapi.io/v1/latest"
        ACCESS_KEY = self.get_AccesKey()                
        exchangeQueryStr = {
            "access_key": "ABCD", #ACCESS_KEY,
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

        if DEBUG:
            print ("Begin request:")
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

    def get_API(self) -> str:
        print ("ExchangeRate Get API ")

        # Make a GET request to the API endpoint
        APIURL = "http://api.exchangeratesapi.io/v1/latest"
        ACCESS_KEY = self.get_AccesKey()  
        rate_data = ""
        exchangeQueryStr = {
            "access_key": ACCESS_KEY,
            "symbols": "EUR,USD,CAD,GBP,JPY,CNY,AUD,HKD,IDR,MXN,SGD,KRW,THB,TWD"
            }

        if DEBUG:
            print (f"Key: {ACCESS_KEY}")
            print ("Begin request:")
        response = requests.get(
            APIURL, 
            params=exchangeQueryStr,
            timeout=2.5
            )
            
        print(f"response code - {response.status_code}")
        if response.status_code == 200: 
            rate_data = response.content
        else: 
            rate_data = self.sample_JSON
            #print (f"error: {self.APIStatusCodes[response.status_code]} ")
        
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
        JSON_data = self.get_API()
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
    
    
