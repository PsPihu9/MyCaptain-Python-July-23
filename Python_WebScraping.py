'''
@author: Prashansa Shah 
@description: Functions in Python
'''
# Task - 

import requests
from bs4 import BeautifulSoup as bs
import pandas
import argparse
import connect

parser = argparse.ArgumentParser
parser.add_argument("--pages", help="Enter the number of pages to parse: ", type=int)
parser.add_argument("--dbname", help="Enter the database to parse: ", type=int)
args = parser.parse_args()

oyo_url = "https://www.oyorooms.com/hotels-in-mumbai/"
pages = args.pages
dbname = args.dbname

connect.connect(dbname)

for page_num in range(1,pages):

    if page_num>1:
        oyo_url = "https://www.oyorooms.com/hotels-in-mumbai/?page="+str(page_num) 

    req = requests.get(oyo_url)
    page_content = req.content
    soup = bs(page_content, 'html.parser')

    all_hotels = soup.find_all("div", {"class":"hotelCardListing"})
    scraped_list = []

    for hotel in all_hotels:

        hotel_dict={}
        hotel_dict["name"] = hotel.find("h3", {"class":"listingHotelDescription__hotelName"}).text
        hotel_dict["address"] = hotel.find("span", {"itemprop":"streetAddress"}).text
        hotel_dict["price"] = hotel.find("span", {"class":"listingPrice__finalPrice"}).text
        hotel_dict["ratings"] = hotel.find("span", {"class":"hotelRating__ratingSummary"}).text

        amenities_element = hotel.find("div", {"class":"amenityWrapper"})
        amenities_list = []
        
        for amenity in amenities_element:
            amenities_list.append(amenity.find("span", {"class":"d-body-sm"}).text.strip())

        hotel_dict["amenities"] = ', '.join(amenities_list[:-1])

        # print("hotel_dict: \n", hotel_dict)
        scraped_list.append(hotel_dict)
        connect.insert_into_table(dbname, tuple(hotel_dict.values()))

    
    # print(oyo_url)

dataFrame = pandas.DataFrame(scraped_list)
dataFrame.to_csv("OyoInMumbai.csv")
connect.get_table_data(dbname)