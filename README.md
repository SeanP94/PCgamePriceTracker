# PC Game Price Tracker

--- 

This is a project that I'm planning on building out to both show some Data Science skills and Data Engineering.


## Format

--- 

To begin, <br>

- I will be using the CheapShark API to track pricing of games. [ X ]
- I will clean and transform the data and move it into a database. [ X ]
- I will be using some form of (hopefully free) cloud computing for this project. [ X ]

- Once this project is complete, I'll be setting up the data ingestion on a Raspberrypi 4 to run on a schedule via Apache Airflow.
  - Slight change of plans to the Airflow implementation. I still want to utilize it. But Cheapshark's API is meant for taking in a users input and getting the data. So what I think will work, is storing user search history by a key, or email. Streamlit allows for user login, so based on this, create a table in SQL that stores a users search history and run it every morning so if the user wants to come back they can see a list of there recent searches, sorted by updates if an item is on sale.
  
 
## Notes

--- 

- This Project is now being integrated into my streamlit site project.
- I as in the last step stated above, I will be continuing to flush out this project so that I can put this on a local Raspberry Pi cluster to have airflow run tasks through it.
  - Not sure if I should wait to get a 2nd Pi before starting a cluster or not :smile: