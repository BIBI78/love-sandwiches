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



#ok i need to find a way to make this work# 
def weekly_schedule():
  # List of exercise options
  exercise_options = ["running", "weightlifting", "yoga", "swimming", "cycling", "boxing"]
  print(exercise_options)
  # Ask user for favorite exercises
  print("What type of exercise do you like to do? (Choose one or more, separate each option with a comma)")
  user_exercise = input().strip().split(",")
  
  # Validate user's exercise choices
  for ex in user_exercise:
    if ex.strip() not in exercise_options:
      print("Invalid option. Please choose from the following:", exercise_options)
      return weekly_schedule()
  
  # Ask user for number of days they want to workout
  print("How many days per week would you like to work out?")
  user_days = input().strip()
  try:
    user_days = int(user_days)
  except ValueError:
    print("Invalid input. Please enter a number.")
    return weekly_schedule()
  
  # Ask user for current weight
  print("What is your current weight (in kg)?")
  user_weight = input().strip()
  try:
    user_weight = float(user_weight)
  except ValueError:
    print("Invalid input. Please enter a number.")
    return weekly_schedule()
  
  # Ask user for desired weight
  print("What is your desired weight (in kg)?")
  user_desired_weight = input().strip()
  try:
    user_desired_weight = float(user_desired_weight)
  except ValueError:
    print("Invalid input. Please enter a number.")
    return weekly_schedule()
  
  # Generate a random weekly schedule
  import random
  days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  random.shuffle(days)
  schedule = []
  for i in range(user_days):
    schedule.append((days[i], random.choice(user_exercise)))
  
  # Print weekly schedule
  print("\nHere is your weekly schedule:")
  for day, ex in schedule:
    print(day, "-", ex)
  
  # Calculate estimated time to reach desired weight
  weight_diff = user_desired_weight - user_weight
  time_to_reach_goal = weight_diff * 1000 / 500 # assuming 500 g weight loss per week
  print("\nIt will take you approximately {:.1f} weeks to reach your desired weight.".format(time_to_reach_goal / 7))


weekly_schedule()