import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

## JSAIS PAS ##
import requests
import json

import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint
from math import ceil

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('1000_sunny_fitness')

def get_user_data():
    weight = float(input("Enter your current weight (in kg): "))
    age = int(input("Enter your age: "))
    height = float(input("Enter your height (in cm): "))
    desired_weight = float(input("Enter your desired weight (in kg): "))
    weight_change = input("Do you want to gain weight or lose weight? (Enter 'gain' or 'Lose'): ")
    
    return weight, age, height, desired_weight, weight_change

def calculate_weight_change_time(weight, age, height, desired_weight, weight_change):
    weight_difference = desired_weight - weight
    time_in_weeks = 0
    if weight_change == "Gain":
        time_in_weeks = weight_difference * 7700 / (height * 6.25)
    elif weight_change == "Lose":
        time_in_weeks = weight_difference * 7700 / (height * 9.25)
    return time_in_weeks

def main():
    weight, age, height, desired_weight, weight_change = get_user_data()
    time_in_weeks = calculate_weight_change_time(weight, age, height, desired_weight, weight_change)
    if weight_change == "Gain":
        print("It will take approximately", time_in_weeks, "weeks to gain", desired_weight - weight, "kg of weight.")
    elif weight_change == "Lose":
        print("It will take approximately", time_in_weeks, "weeks to lose", weight - desired_weight, "kg of weight.")

if __name__ == "__main__":
    main()