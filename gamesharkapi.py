"""
File for the GameSharkAPI class
Holds all functionality and logging for the class.

TEMPORARY:
Will be the main driver as I test this class and build it out.

"""
from time import sleep # Need to make sure we pause for a second after every API call
import requests
import json
import logging

# Setup error Logging.
logging.basicConfig(filename='requestsError.log', encoding='utf-8', level=logging.ERROR)



class GameSharkAPI:
    def __init__(self):
        self.baseUrl = "https://www.cheapshark.com/api/1.0/"
        self.payload={}
        self.headers = {}
    
    def requestTest(self, url="https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=15"):
        """Function to test and list the data from the testing url
        Will print the first 5 of the request only, otherwise will log an error
        
        Keyword arguments:
        url: Url to test, base one is the test one from the website.
        """
        jsonData = self.requestTest(url)
        if jsonData != None: 
            self.printJson(json)
    
    def requestUrl(self, url) :
        """Class to pass in a url to get the json data back.

        Keyword arguments:
        url: Url for the location we'd like to request data from.
        
        Returns:
        On Success -> json(dictionary) of the requested data
        On Failure -> None
        """
        try:
            sleep(1) # Pauses for 1 second in between any call
            response = requests.request("GET", url, headers=self.headers, data=self.payload)
            assert 200 == response.status_code
            return response.json()
        except:
            logging.error(f"ERROR: Did not recieve code 200, recieved code {response.status_code}; URL: {url}")
            print(f"ERROR: Did not recieve code 200, recieved code {response.status_code}; URL: {url}")
            return None# Return None if we have an error.
    
    def printJson(self, jsonData: dict):
        """Prints the contents of a request.
        
        Keyword arguments:
        jsonData: a dictionary that contains the contents of a file to print. 
        """
        for data in jsonData:
            print(json.dumps(data, indent=4))



gsa = GameSharkAPI()
gsa.requestTest()