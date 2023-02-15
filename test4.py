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
    return days_needed 

## OK NOW I EDIT##
def get_user_data():
    print("Please answer the following questions\n")
    age = int(input("Enter your age: "))
    height = float(input("Enter your height (in cm): "))
    weight = float(input("Enter your current weight (in kg): "))
    desired_weight = float(input("Enter your desired weight (in kg): "))
    weight_change = input("Do you want to gain weight or lose weight? (Enter gain or lose'): ")
    
    return weight, age, height, desired_weight, weight_change

def calculate_weight_change_time(weight, age, height, desired_weight, weight_change):
    weight_difference = desired_weight - weight
    time_in_weeks = 0
    if weight_change == "gain":
         BMR = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
         weight_gain_time = BMR * 1.55
         time_to_reach_desired_weight = (desired_weight - weight) / 0.5
         time_needed = (desired_weight - weight) / 0.5
    elif weight_change == "lose":
        weight_loss_rate = weight - desired_weight
        deficit_needed = weight_loss_rate * 7700
        recomended_deficit = (10*(weight) + 6.25*(height) -(5*age)+5)
        deficit_per_day = recomended_deficit 
        days_needed = deficit_needed / deficit_per_day
        recomended_deficit = (10*(weight) + 6.25*(height) -(5*age)+5)
        #days need#
        deficit_needed = recomended_deficit
        time_needed = recomended_deficit
    return time_needed

def main():
    weight, age, height, desired_weight, weight_change = get_user_data()
    
    time_in_weeks = calculate_weight_change_time(weight, age, height, desired_weight, weight_change)
    calories_per_day = calculate_weight_change_time(weight, age, height, desired_weight, weight_change)

    ## all this is for weight loss calculations ##
    ## this is stupid bcause it seems like im rewriting my code again outside the function i already defined##
    weight_loss_rate = weight - desired_weight 
    deficit_per_day = (10*(weight) + 6.25*(height) -(5*age)+5)
    deficit_needed = weight_loss_rate * 7700
    days_needed = deficit_needed / deficit_per_day

    if weight_change == "gain":
        print("it will take you", time_in_weeks,"weeks to gain", desired_weight - weight, "kg of weight.")
    elif weight_change == "lose":
        print("you should eat", calories_per_day,"for" , days_needed, "days to lose", weight - desired_weight, "kg of weight.")

if __name__ == "__main__":
    main()