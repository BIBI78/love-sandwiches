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



def weight_loss_time(weight, desired_weight,age,height):
    weight_loss_rate = weight - desired_weight
    deficit_needed = weight_loss_rate * 7700
    recomended_deficit = (10*(weight) + 6.25*(height) -(5*age)+5)
    deficit_per_day = recomended_deficit 
    days_needed = deficit_needed / deficit_per_day
    recomended_deficit = (10*(weight) + 6.25*(height) -(5*age)+5)
    deficit_needed = recomended_deficit
    #user_data = (weight,height,age,desired_weight)
    return days_needed , (name, age)

def weight_gain_time(weight, height, age, desired_weight):
    BMR = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    weight_gain_time = BMR * 1.55
    time_to_reach_desired_weight = (desired_weight - weight) / 0.5
    return weight_gain_time, time_to_reach_desired_weight

def weight_change():
    weight_change = input("WELCOME TO 1000 SUNNY FITNESS \n Would you like to lose or gain weight? (lose or gain): \n")
    name = input("What's your name? \n")
    age = int(input("Enter your age: \n "))
    height = float(input("Enter your height (in cm): \n"))
    weight = float(input("Enter your current weight in kg:\n "))
    desired_weight = float(input("Enter your desired weight in kg: \n"))

    while True:
        
        if weight_change == "lose":
            recomended_deficit = (10*(weight) + 6.25*(height) -(5*age)+5)
            time = weight_loss_time(weight, desired_weight,age,height)
            print(f"You should eat about  {recomended_deficit} calories per day for about {time} days")
            deficit_per_day = recomended_deficit 
            weight_loss_time(weight, desired_weight,age,height)
            user_data = (weight,height,age,desired_weight)
            break
        elif weight_change == "gain":
            calories_per_day, time_to_reach_desired_weight = weight_gain_time(weight, height, age, desired_weight)
            print("To gain this weight, you should eat about", ceil(calories_per_day), "calories per day.")
            print("and will take approximately {} weeks to reach your desired weight.".format(time_to_reach_desired_weight))
            weight_gain_time(weight, height, age, desired_weight)
            user_data = (weight,height,age,desired_weight)
            break
        else:
            print("Invalid response, please enter either 'lose' or 'gain'")



def print_info(info):
  name, age,desired_weight,height = info
  print(f"Your name is {name} and you're {age} years old.")




# IM TRYIMG TO GET THE VALUES THAT ARE CALCULATED IN THE FUNCTION OUT , SO I CAN MANIPULATE THEM #
def main():
    name = input("What's your name? \n")
    age = int(input("Enter your age: \n "))
    weight_change()
    #print(f" {name} and you're {age} years old.")
   
    info = weight_loss_time(weight, desired_weight, age, height)
    print_info(info)


main()