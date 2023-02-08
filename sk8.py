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
    print(f"Your the recommened deficit is {recomended_deficit} ")
 

#user_info()
info = user_info()
#print_user_info(info)
print_user_weight_loss_info(info)

