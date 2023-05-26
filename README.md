# PC Game Price Tracker

This is a project that I'm planning on building out to both show some Data Science skills and Data Engineering.


## Format

To begin, <br>

- I will be using the CheapShark API to track pricing of games. [ ]
- I will clean and transform the data and move it into a database. [ ]
- I will be using some form of (hopefully free) cloud computing for this project. [ ]
  - Debating on using AWS, otherwise I'll use something like Firebase, but for SQL. (Still need to research this.)
    - (I've used Firebase for a school project before, so I rather use SQL for this project so that I can clean and utilize the data differently.)
  - Eventually, it will be on the cloud. In the beginning it will be hosted locally while I work through it and get more comfortable with.
  - I would LOVE to use Spark and Databricks for this project. So as I progress I will possibly adjust to this
- Once this project is complete, I'll be setting up the data ingestion on a Raspberrypi 4 to run on a schedule via Apache Airflow.
- Finally for visualizing the information(This will be a seperate repo), I will either create a Kotlin App, or I will host the information on a website created with pythons Streamlit library. 
 

 ## Notes
- This project will pull from a file called SECRETS.json that will store anything private. This will not be available in the github repo but I will show the format of the Json file below