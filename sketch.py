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

# Pirate flag #
def draw_jolly_roger():
    """
    draws pirate flag
    """
    print("WELCOME TO THE 1000 SUNNY")
    jolly_roger =  '.=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-.\n'
    jolly_roger += '|                     ______                     |\n'
    jolly_roger += '|                  .-"      "-.                  |\n'
    jolly_roger += '|                 /            \                 |\n'
    jolly_roger += '|     _          |              |          _     |\n'
    jolly_roger += '|    ( \         |,  .-.  .-.  ,|         / )    |\n'
    jolly_roger += '|     > "=._     | )(__/  \__)( |     _.=" <     |\n'
    jolly_roger += '|    (_/"=._"=._ |/     /\     \| _.="_.="\_)    |\n'
    jolly_roger += '|           "=._"(_     ^^     _)"_.="           |\n'
    jolly_roger += '|               "=\__|IIIIII|__/="               |\n'
    jolly_roger += '|              _.="| \IIIIII/ |"=._              |\n'
    jolly_roger += '|    _     _.="_.="\          /"=._"=._     _    |\n'
    jolly_roger += '|   ( \_.="_.="     `--------`     "=._"=._/ )   |\n'
    jolly_roger += '|    > _.="                            "=._ <    |\n'
    jolly_roger += '|   (_/   free young thug                  \_)   |\n'
    jolly_roger += '|                                                |\n'
    jolly_roger += '.=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-.\n'
    print(jolly_roger)


#1
def weight_loss_time(weight, desired_weight,age,height):
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
#2

def weight_gain_time(weight, height, age, desired_weight):
    """
    calculates ursers weigh gain projection
    """
    # this is the bmr for weight loss 
    BMR = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    weight_gain_time = BMR * 1.55
    time_to_reach_desired_weight = (desired_weight - weight) / 0.5
    #user_data = (weight,height,age,desired_weight)
    return weight_gain_time, time_to_reach_desired_weight


def weight_change():
    while True:
        weight_change = input("WELCOME TO 1000 SUNNY FITNESS \n Would you like to lose or gain weight? (lose or gain): \n")
        if weight_change == "lose":
            print("Please answer the following questions\n")
            weight = float(input("Enter your current weight in kg:\n "))
            height = float(input("Enter your height (in cm): \n"))
            age = int(input("Enter your age: "))
            recomended_deficit = (10*(weight) + 6.25*(height) -(5*age)+5)
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


# is this function storing user data in the spread sheet. ?# 
# NOOOOOOO #
def stored_user_data():
    weight, age , height,desired_weight = weight_change()
    user_data = (weight,height,age,desired_weight)
    return user_data,




# USE THIS TO VALIDATE DATA #
def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 4:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True





# DECLARE GLOBAL VARIABLES HERE?? #
 #user_data = (weight,height,age,desired_weight)
 # maybe define user ddata and weight in another fucntion that does ask the user anything in the terminal 






            
   

    
  # NOTE #
  # still need to figure out how to change color of text in terminal#
    


#main()

# 5 
## new code janvier 23 2023 ##
def exercise_suggestions():
    exercise_type = input("What type of exercises qre you into?? (cardio, strength, yoga) ")
    if exercise_type.lower() == "cardio":
        print("Try going for a run , boxingn or some type of martial arts.")
    elif exercise_type.lower() == "strength":
        print("Try lifting weights at the gym")
    elif exercise_type.lower() == "yoga":
        print("Try a yoga class, doing a yoga video at home, or going for a yoga hike.")
    else:
        print("SORRY   enter something that makes sense wesh.")

# exercise_suggestions()
# I should get a value here anc store it somehwer# 


### I want to take all this data and return a weekly schedlue#

# function 6
def workout_plan():
    workout_frequency = input("How often would you like to work out each week?")
    if "3" in workout_frequency or "three" in workout_frequency:
        print("A good plan would be to work out Monday, Wednesday, and Friday.")
    elif "4" in workout_frequency or "four" in workout_frequency:
        print("A good plan would be to work out Monday, Tuesday, Thursday, and Friday.")
    elif "5" in workout_frequency or "five" in workout_frequency:
        print("A good plan would be to work out Monday through Friday.")
    elif "6" in workout_frequency or "six" in workout_frequency:
        print("A good plan would be to work out Monday through Saturday.")
    elif "7" in workout_frequency or "seven" in workout_frequency:
        print("A good plan would be to work out every day.")
    else:
        print("Sorry, I don't understand your input.")

#workout_plan()

def workout_schedule():
    #Ask user for types of exercises they like
    exercise_types = input("What types of exercises do you like? (e.g. cardio, strength, yoga) ")

    #Ask user for how many days they would like to work out
    workout_days = int(input("How many days per week would you like to work out? "))

    #Ask user for their current weight
    current_weight = float(input("What is your current weight in kg? "))

    #Ask user for their desired weight
    desired_weight = float(input("What is your desired weight in kg? "))

    #Calculate calorie deficit needed per day to reach desired weight
    calorie_deficit = (current_weight - desired_weight) * 7700

    #Create empty dictionary for workout schedule
    schedule = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": [], "Saturday": [], "Sunday": []}

    #Populate workout schedule with exercise types
    for i in range(workout_days):
        day = input(f"Which day do you want to work out? (e.g. Monday) ")
        schedule[day.capitalize()].append(exercise_types)
    # Print the schedule
    print("Here is your weekly workout schedule:")
    for day, workout in schedule.items():
        if workout:
            print(f"{day}: {workout}")
        else:
            print(f"{day}: Rest Day")



#workout_schedule()

# NOTE #
# need to add somehting that qhen the user inputs a value not in the lost nof values #


# try dis #

def workout_schedule():
    valid_exercise_types = ["cardio", "strength", "yoga"]
    valid_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    #Ask user for types of exercises they like
    exercise_types = input("What types of exercises do you like? (e.g. cardio, strength, yoga) ")
    while exercise_types.lower() not in valid_exercise_types:
        print("Invalid input, Please choose from: cardio, strength, yoga")
        exercise_types = input("What types of exercises do you like? (e.g. cardio, strength, yoga) ")
    #Ask user for how many days they would like to work out
    workout_days = int(input("How many days per week would you like to work out? "))
    #Ask user for their current weight
    current_weight = float(input("What is your current weight in kg? "))
    #Ask user for their desired weight
    desired_weight = float(input("What is your desired weight in kg? "))
    #Calculate calorie deficit needed per day to reach desired weight
    calorie_deficit = (current_weight - desired_weight) * 7700
    #Create empty dictionary for workout schedule
    schedule = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": [], "Saturday": [], "Sunday": []}
    #Populate workout schedule with exercise types
    for i in range(workout_days):
        day = input(f"Which day do you want to work out? (e.g. Monday) ")
        while day.capitalize() not in valid_days:
            print("Invalid input, Please choose from: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday")
            day = input(f"Which day do you want to work out? (e.g. Monday) ")
        schedule[day.capitalize()].append(exercise_types)
    # Print the

#main()
#workout_schedule()

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


def main ():
    draw_jolly_roger()
    weight_change()
    #stored_user_data() does not work ?

#main()
#weekly_schedule()

#workout_schedule()
weight_change()