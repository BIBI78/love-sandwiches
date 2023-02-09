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


#1
# I NEED TO GET ALL THE INFO I NEED TO MANIPULATE HERE ?? #
def user_info():
  name = input("What's your name? \n")
  age = int(input("Enter your age: \n "))
  height = float(input("Enter your height (in cm): \n"))
  weight = float(input("Enter your current weight in kg:\n "))
  desired_weight = float(input("Enter your desired weight in kg: \n"))
  return(name,age,weight,desired_weight,height)



  #2
  def weight_loss_time(weight, desired_weight,age,height,name):
    """"
    calculates users weight loss projection
    """
    weight_loss_rate = weight - desired_weight
    deficit_needed = weight_loss_rate * 7700
    recomended_deficit = (10*(weight) + 6.25*(height) -(5*age)+5)
    deficit_per_day = recomended_deficit 
    days_needed = deficit_needed / deficit_per_day
    recomended_deficit = (10*(weight) + 6.25*(height) -(5*age)+5)
    deficit_needed = recomended_deficit
    #user_data = (weight,height,age,desired_weight)
    return days_needed


def print_user_info(info):
  name, age, weight,desired_weight,height = info
  print(f"Your name is {name} and you're {age} years old. and your current weight is {weight} years old.and your desired weight is {desired_weight} . you height {height}")


# i need another function like print user
def print_user_weight_loss_info(info):
    name, age, weight,desired_weight,height = info
    weight_loss_rate = weight - desired_weight
    deficit_needed = weight_loss_rate * 7700
    recomended_deficit = (10*(weight) + 6.25*(height) -(5*age)+5)
    deficit_per_day = recomended_deficit 
    days_needed = deficit_needed / deficit_per_day
    recomended_deficit = (10*(weight) + 6.25*(height) -(5*age)+5)
    deficit_needed = recomended_deficit
    
    print(f"Your the recommened deficit per day is {deficit_per_day} ")
 
# SHOULD I DEFINE A MAIN FUNCTION ??, HARD TO SET VARIABLES"
#user_info()
#print_user_info(info)
#print_user_weight_loss_info(info)

def weight_change():
    while True:
        weight_change = input("WELCOME TO 1000 SUNNY FITNESS \n Would you like to lose or gain weight? (lose or gain): \n")
        if weight_change == "lose":
            print("Please answer the following questions\n")
            weight = float(input("Enter your current weight in kg:\n "))
            desired_weight = float(input("Enter your desired weight in kg: \n"))
            height = float(input("Enter your height (in cm): \n"))
            age = int(input("Enter your age: "))
            recomended_deficit = (10*(weight) + 6.25*(height) -(5*age)+5)
            ### PROBLEM HERE ####
            time = weight_loss_time(weight, desired_weight,age,height) 
            print(f"You should eat about  {recomended_deficit} calories per day for about {time} days")
            deficit_per_day = recomended_deficit 
            weight_loss_time(weight, desired_weight,age,height)
            user_data = (weight,height,age,desired_weight)
            break
        elif weight_change == "gain":
            print("Please answer the following questions\n")
            weight = float(input("Enter your current weight (in kg): \n"))
            height = float(input("Enter your height (in cm): \n"))
            age = int(input("Enter your age: "))
            desired_weight = float(input("Enter the weight youd like to build up to (in kg): \n"))
            calories_per_day, time_to_reach_desired_weight = weight_gain_time(weight, height, age, desired_weight)
            print("To gain this weight, you should eat about", ceil(calories_per_day), "calories per day.")
            print("and will take approximately {} weeks to reach your desired weight.".format(time_to_reach_desired_weight))
            weight_gain_time(weight, height, age, desired_weight)
            user_data = (weight,height,age,desired_weight)
            break
        else:
            print("Invalid response, please enter either 'lose' or 'gain'")

def main():
    #weight_change()
    info = user_info()
    print_user_weight_loss_info(info)
    
main()

