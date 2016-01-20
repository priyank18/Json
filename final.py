"""------This is a python program that scrapes information 
from a website and stores data in JSON file---------"""
import requests
import json
from bs4 import BeautifulSoup

#Getting the URL's data and passing it to  BeautifulSoup.
url = "http://52.8.18.83/companies/Stehr,%20Beahan%20and%20Spencer" 
html = requests.get(url)
soup = BeautifulSoup(html.content)

#Creating a Dictionary to search the required data and store it. 
data ={"name":" ", "street_address":" ", "street_address_2":" ", "city":" ", "state":" ", "zipcode":" ", "phone_number":" ", "website":" ", "description":" "}
for key in data:
   data[key] = soup.find(id=key).string

#Writing the scraped data onto a JSON File.
with open('data.json','w') as outfile:
   json.dump(data,outfile)
print "\nprocess complete!\n"

#===================END====================#
