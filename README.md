# PC Game Price Tracker

This is a project that I'm planning on building out to both show some Data Science skills and Data Engineering.


## Format

To begin, <br>

- I will be using the CheapShark API to track pricing of games. [ ]
- I will clean and transform the data and move it into a database. [ ]
- I will be using some form of (hopefully free) cloud computing for this project. [ ]
  - Eventually, it will be on the cloud. In the beginning it will be hosted locally while I work through it and get more comfortable with.
    - Looking into Bluehost or Hostinger. I want to avoid using AWS until I've professionally used it. And this way I can make sure I have both a SQL server (MySQL) and a websitehost (Website might be hosted directly on Streamlit) and it will be a set 3$ a month.
  - I would LOVE to use Spark for this project. If not I'll design my own pipeline with Pandas.

- Once this project is complete, I'll be setting up the data ingestion on a Raspberrypi 4 to run on a schedule via Apache Airflow.
  - Slight change of plans to the Airflow implementation. I still want to utilize it. But Cheapshark's API is meant for taking in a users input and getting the data. So what I think will work, is storing user search history by a key, or email. Streamlit allows for user login, so based on this, create a table in SQL that stores a users search history and run it every morning so if the user wants to come back they can see a list of there recent searches, sorted by updates if an item is on sale.
  
- Finally for visualizing the information(This will be a seperate repo), I will either create a Kotlin App, or I will host the information on a website created with pythons Streamlit library. 
 

## Notes
- This project will pull from a file called SECRETS.json that will store anything private. This will not be available in the github repo but I will show the format of the Json file below

## Questions
- Can I use NLP to search for games via the API? 