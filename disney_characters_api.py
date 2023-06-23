import requests
import pprint
import pandas as pd
import sqlalchemy as db

def get_formt(s): 
    return input_name.replace(" ", "%20")

def get_data(s):
    response = requests.get(f"https://api.disneyapi.dev/character?name={s}")
    return response.json()

def display_data(s):
    print("------------------------------------")
    print(f"\nSome films that {s} is in are...\n")

    i = 1
    for values in data['data'][1]['films']:
        print(f"{i}: {values}\n")
        i += 1

    if len(data['data'][1]['films']) == 0:
        print(f"Could not find {s}")

    print("-----------------------------------")

input_name = input("Enter Character Name: ")
name = get_formt(input_name)
data = get_data(name)
display_data(input_name)



