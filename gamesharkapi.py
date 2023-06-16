"""
File for the GameSharkAPI class
Holds all functionality and logging for the class.

TEMPORARY:
Will be the main driver as I test this class and build it out.
Test
"""
from time import sleep # Need to make sure we pause for a second after every API call
import requests
import json
import logging
import re
import mysql.connector
import json
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
        jsonData = self.requestUrl(url).json()
        if jsonData != None: 
            self.printJson(jsonData[:5])
        return jsonData

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
            return response
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

    def goToDeal(self, dealId:str):
        """Takes in a dealId and sends you to the link through
        cheapsharks portal (Used to help them get a credit for the
        sale, if bought, terms of using the API for free.)
        """

        dealId="liaqeBQtozzs0vzBu8CY9pN78c4rUdHcSdL2SnDowhA%3D"
        dealUrl = f"https://www.cheapshark.com/redirect?dealID={dealId}"
        
        # This will be replaced later with functionality in streamlit
        # NOTE: This is really slow to open a browser in WSL.
        #       Keep the WSL chrome browser open after first run.
        #       For faster testing
        
        import webbrowser  
        webbrowser.open(dealUrl, new=0, autoraise=True)
    
    def getAllDeals(self):
        """Get all deals from Cheapshark Api.
        TODO: 
            1. This will feed the data into PySpark. 
            2. Figure out how to get the entire list, since you get the data in pages.
        """
        initRun = self.baseUrl + f"deals?"
    
    def getStoreIds(self):
        storeUrl = self.baseUrl + "stores"
        jsonObj = self.requestUrl(storeUrl)
        self.printJson(jsonData=jsonObj.json())    
        
    def getMaxDealPages(self, **argv):
        """Uses the test to get the max amount of pages.
        """
        
        title = "" if not argv.get("title") else f"&title={argv['title']}"

        data = self.requestUrl(url=f"https://www.cheapshark.com/api/1.0/deals?pageSize=60&pageNumber=0{title}")
        if data == None:
            return
        self.printJson(data.json())

        
        print(data.headers['X-Total-Page-Count'])
        print(len(data.json()))

    def searchGame(self, userInput):
        """Runs a query to the API to search for a game given a parameter.
        converts the userInput into a format the API recognizes.
        """
        userInput = userInput.strip().replace(" ", "%20").upper()
        self.getMaxDealPages(title=userInput)
        


class SqlInteractions:
    
    def __init__(self):
        """
        Launches the sql object
        Initializes core functionality and creates a self.__cur object.
        """

    def nonCommitWrapper(func):
        """
        Singular Input, resets the 
        """
        def wrapper(self, *x):
            with open(".secrets.json", 'r') as f:
                data = json.load(f)
                connection = mysql.connector.connect(
                    host=data['host'],
                    database=data["database"],
                    user=data['user'],
                    passwd=data['password']
                )
                del data # We want to not keep .secrets in memory :) 
            self.__cur = connection.cursor()
            
            print("Opening Connection.")
            if len(x) > 0:
                func(self, *x)
            else:
                func(self)
            print("Closing Connection.")
            self.__cur.close()
        return wrapper

    @nonCommitWrapper
    def getTableNames(self):
        """
        Used to return the table names for the class to function properly
        """
        self.__curr.execute("""
        SHOW TABLES;
        """)
        self.__curr.fetchall()
    
    @nonCommitWrapper
    def getTableNames2(self, z):
        """
        Used to return the table names for the class to function properly
        """
        
    def getTableCopy(tableName):
        pass

# test = SqlInteractions()
# test.getTableNames()