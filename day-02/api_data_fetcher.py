import requests
import json

api_key = "7361bd5b1c8b454695a63280d64cb810"
api_url ="https://phoneintelligence.abstractapi.com/"

phone_number = input("Enter your phone number with country code: ")

def get_phone_number_details(phone_number):

    query = f"v1/?api_key={api_key}&phone={phone_number}"
    responce = requests.get(url=api_url+query)
    for key, value in responce.json().items():
        if key == "phone_location":
            print(key,value)


get_phone_number_details(phone_number)