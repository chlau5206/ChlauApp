''' API Exchange Rate.py
'''
import os
import json
# import shutil
# import urllib
# import urllib3

import requests 
from datetime import date, datetime
from dotenv import load_dotenv

DEBUG = False

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

        self.sample_JSON = b'{"success":false,"timestamp":1763580847,"base":"EUR","date":"2000-01-01","rates":{"EUR":1,"USD":1.152538,"CAD":1.620267,"GBP":0.882942,"JPY":180.783096}}'

        ## Replace single quotes with double quotes (JSON standard)
        # self.sample_JSON = self.sample_JSON.replace("'", '"')
        
        if os.path.exists(".env.dev"):
            load_dotenv(dotenv_path=".env.dev")
            print (".env.dev loaded.")
        else:     
            load_dotenv()
            print (".env loaded.")

        self.project_path = os.getenv("PROJECT_PATH")
        self.latest_file = os.path.join(self.project_path,
                                        "Projects", "ExchangeRates", "static","data",
                                        "LatestRate.json")

    def get_AccesKey(self) -> str:
        if DEBUG:
            print ('Get Access Key')
        try: 
            key = os.getenv("API_KEY")
                
        except OSError as e:
            print (f"OSExcept #{e.errno}:{e.strerror} -- {e.filename} ")
        except Exception as e:
            print (f"Error: {e}")
        
        return key
 
    def get_API(self) -> str:
        if DEBUG:
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
            print (f"Debug: {DEBUG}")
            print (f"API URL: {APIURL}")
            print ("params: ", exchangeQueryStr)
            print ("Begin API request:")
        response = requests.get(
            APIURL, 
            params=exchangeQueryStr,
            timeout=2.5
            )
            
        if response.status_code == 200: 
            rate_data = response.content
        else: 
            rate_data = self.sample_JSON
            print(f"Error:{response.status_code}-{self.APIStatusCodes[str(response.status_code)]}")

        return rate_data.decode('utf-8')  # convert to utf-8 string

    def getExchangeRate(self):
        print ("ExchangeRate get rate")
        
        JSON_data = self.get_API()
        if DEBUG:
            if JSON_data:
                print ("Print JSON_data: ")
                JSON_Print(JSON_data)
            else: 
                print ("JSON_data is empty.")
        try:
            today_date = date.today().isoformat()
            # today_date = JSON_data.get('date')
            todayFile = os.path.join(self.project_path,
                                     "Projects", "ExchangeRates", "static","data",
                                    "ExchangeRate_" + today_date + ".json")
            
            if DEBUG:
                with open(todayFile, 'w') as writeFile:
                    writeFile.write(JSON_data)
                    writeFile.close()
                print (f"Today file {todayFile} saved.")

            with open(self.latest_file, 'w') as LatestFile:
                LatestFile.write(JSON_data)
                LatestFile.close()
            print (f"Latest File, {self.latest_file} saved.")

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

def JSON_Print(obj):
    print(json.dumps(json.loads(obj), sort_keys=True, indent=4))

if __name__=="__main__":
    EX = ExchangeRateOps()
    response = EX.getExchangeRate()
