import pymongo
import urllib.parse
import pandas as pd
import json
from pymongo import MongoClient
from pymongo.server_api import ServerApi

# MongoDB connection string (replace <password> with your actual password)
uri = "mongodb+srv://FreddyBolshack:eHuUgEWoXVTU7Fso@plantinfo.8dghkgg.mongodb.net/?retryWrites=true&w=majority&appName=PlantInfo"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

try:
    # Read data from an Excel file into a pandas DataFrame
    data = pd.read_excel("C:/sourcecode/New folder/sample.xlsx", sheet_name="Prices")
    
    # Convert DataFrame to a list of dictionaries (records)
    json_result = data.to_dict(orient='records')
    
    # Database and collection details
    #creating empty dataase and collection
    myDb = client["PlantInfo"]
    myCol = myDb["PlantPrices"]
    
    # Iterate over each item in the json_result list
    for item in json_result:
        # Extract relevant fields from the item dictionary
        commodity = item.pop("Commodity")
        size = item.pop("Size")
        currency = item.pop("Currency")
        unit = item.pop("Unit")
        yearly_average = item.pop("Yearly Average")
        
        # Create a dictionary for monthly prices, excluding other fields
        monthly_prices = {month: item[month] for month in item} 
        
        # Construct the document to be inserted into MongoDB
        priceEntry = {
            commodity: {
                "Unit": unit,
                "Size": size,
                "Currency": currency,
                "MonthlyPrices": monthly_prices
            }
        }
        
        # Insert a single document into the MongoDB collection
        myCol.insert_one(priceEntry)
#catches errors
except Exception as e:
    print(e)
