import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint
import requests
import json
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



import random
import time

def workout3_schedule():
    options = {
        'cardio': ['treadmill', 'elliptical', 'stairmaster'],
        'weight lifting': ['bench press', 'squat', 'deadlift'],
        'home exercise': ['push-ups', 'crunches', 'lunges']
    }
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Prompt user for exercise types
    exercise_types = []
    while True:
        exercise_choice = input(f"What types of exercise would you like to do? (Choose 1, 2 or all 3): {', '.join(options.keys())} ")
        if exercise_choice == '1':
            exercise_types = random.sample(list(options.keys()), 1)
            break
        elif exercise_choice == '2':
            exercise_types = random.sample(list(options.keys()), 2)
            break
        elif exercise_choice == 'all':
            exercise_types = list(options.keys())
            break
        print("Invalid input, please choose again.")
    
    # Prompt user for exercise options
    chosen_options = {}
    for exercise in exercise_types:
        while True:
            option_choice = input(f"What {exercise} exercise would you like to do? (Choose 1, 2 or all 3): {options[exercise]} ")
            if option_choice == '1' or option_choice == '2' or option_choice == 'all':
                if option_choice == '1':
                    chosen_options[exercise] = [random.choice(options[exercise])]
                elif option_choice == '2':
                    chosen_options[exercise] = random.sample(options[exercise], 2)
                else:
                    chosen_options[exercise] = options[exercise]
                break
            print("Invalid input, please choose again.")
    
    # Prompt user for number of days per week
    while True:
        try:
            num_days = int(input("How many days per week would you like to work out? "))
            if num_days < 1 or num_days > 7:
                raise ValueError
            break
        except ValueError:
            print("Invalid input, please enter a number between 1 and 7.")
    
    # Create workout schedule
    schedule = {}
    for day in days:
        schedule[day] = []
    for i in range(num_days):
        while True:
            day_choice = input(f"Enter day {i+1} of your workout schedule (e.g. Monday): ")
            if day_choice in days:
                if chosen_options:
                    exercise_choice = random.choice(chosen_options[day_choice.split()[0].lower()])
                else:
                    exercise_choice = random.choice(list(options.values())[0])
                schedule[day_choice].append(exercise_choice)
                break
            print("Invalid input, please choose a valid day.")
    
    # Print workout schedule
    print("Here's your workout schedule:")
    for day, exercises in schedule.items():
        if exercises:
            print(f"{day}: {', '.join(exercises)}")
        else:
            print(f"{day}: Rest")
        time.sleep(0.5)  # Add a small delay for better readability


##workout3_schedule()

import random
import time

def workout4_schedule():
    options = {
        'cardio': ['treadmill', 'elliptical', 'stairmaster'],
        'weight lifting': ['bench press', 'squat', 'deadlift'],
        'home exercise': ['push-ups', 'crunches', 'lunges']
    }
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Prompt user for exercise types
    exercise_types = []
    while True:
        exercise_choice = input(f"What types of exercise would you like to do? (Choose one, two, or all): {', '.join(options.keys())} ")
        if exercise_choice == 'one':
            exercise_types.append(random.choice(list(options.keys())))
            break
        elif exercise_choice == 'two':
            while len(exercise_types) < 2:
                choice = input(f"Choose an exercise type: {', '.join(options.keys())} ")
                if choice in options.keys() and choice not in exercise_types:
                    exercise_types.append(choice)
            break
        elif exercise_choice == 'all':
            exercise_types = list(options.keys())
            break
        print("Invalid input, please choose again.")
    
    # Prompt user for exercise options
    chosen_options = {}
    for exercise in exercise_types:
        while True:
            option_choice = input(f"What {exercise} exercise would you like to do? (Choose 1, 2 or all 3): {options[exercise]} ")
            if option_choice == '1' or option_choice == '2' or option_choice == 'all':
                if option_choice == '1':
                    chosen_options[exercise] = [random.choice(options[exercise])]
                elif option_choice == '2':
                    chosen_options[exercise] = random.sample(options[exercise], 2)
                else:
                    chosen_options[exercise] = options[exercise]
                break
            print("Invalid input, please choose again.")
    
    # Prompt user for number of days per week
    while True:
        try:
            num_days = int(input("How many days per week would you like to work out? "))
            if num_days < 1 or num_days > 7:
                raise ValueError
            break
        except ValueError:
            print("Invalid input, please enter a number between 1 and 7.")
    
    # Create workout schedule
    schedule = {}
    for day in days:
        schedule[day] = []
    for i in range(num_days):
        while True:
            day_choice = input(f"Enter day {i+1} of your workout schedule (e.g. Monday): ")
            if day_choice in days:
                if chosen_options:
                    exercise_choice = random.choice(chosen_options[day_choice.split()[0].lower()])
                else:
                    exercise_choice = random.choice(list(options.values())[0])
                schedule[day_choice].append(exercise_choice)
                break
            print("Invalid input, please choose a valid day.")
    
    # Print workout schedule
    print("Here's your workout schedule:")
    for day, exercises in schedule.items():
        if exercises:
            print(f"{day}: {', '.join(exercises)}")
        else:
            print(f"{day}: Rest")
        time.sleep(0.5)  # Add a small delay for better readability

#workout4_schedule()


import random
import time

def workout5_schedule():
    options = {
        'cardio': ['treadmill', 'elliptical', 'stairmaster'],
        'weight lifting': ['bench press', 'squat', 'deadlift'],
        'home exercise': ['push-ups', 'crunches', 'lunges']
    }
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Prompt user for exercise types
    exercise_types = []
    while True:
        exercise_choice = input("What exercises would you like to do? (Enter 'cardio', 'weight lifting', or 'home workout') ")
        if exercise_choice in options.keys() and exercise_choice not in exercise_types:
            exercise_types.append(exercise_choice)
            if len(exercise_types) == 3:
                break
            else:
                another_choice = input("Is that all? (Enter 'yes' or 'no') ")
                if another_choice.lower() == 'yes':
                    break
        elif exercise_choice not in options.keys():
            print("Invalid input, please enter a valid exercise type.")
    
    # Prompt user for exercise options
    chosen_options = {}
    for exercise in exercise_types:
        while True:
            option_choice = input(f"What {exercise} exercise would you like to do? (Choose 1, 2 or all 3): {options[exercise]} ")
            if option_choice == '1' or option_choice == '2' or option_choice == 'all':
                if option_choice == '1':
                    chosen_options[exercise] = [random.choice(options[exercise])]
                elif option_choice == '2':
                    chosen_options[exercise] = random.sample(options[exercise], 2)
                else:
                    chosen_options[exercise] = options[exercise]
                break
            print("Invalid input, please choose again.")
    
    # Prompt user for number of days per week
    while True:
        try:
            num_days = int(input("How many days per week would you like to work out? "))
            if num_days < 1 or num_days > 7:
                raise ValueError
            break
        except ValueError:
            print("Invalid input, please enter a number between 1 and 7.")
    
    # Create workout schedule
    schedule = {}
    for day in days:
        schedule[day] = []
    for i in range(num_days):
        while True:
            day_choice = input(f"Enter day {i+1} of your workout schedule (e.g. Monday): ")
            if day_choice in days:
                if chosen_options:
                    exercise_choice = random.choice(chosen_options[day_choice.split()[0].lower()])
                else:
                    exercise_choice = random.choice(list(options.values())[0])
                schedule[day_choice].append(exercise_choice)
                break
            print("Invalid input, please choose a valid day.")
    
    # Print workout schedule
    print("Here's your workout schedule:")
    for day, exercises in schedule.items():
        if exercises:
            print(f"{day}: {', '.join(exercises)}")
        else:
            print(f"{day}: Rest")
        time.sleep(0.5)  # Add a small delay for better readability

#workout5_schedule()

def get_workout_plan():
    exercises = []
    options = ["cardio", "weight lifting", "home workout"]
    while len(exercises) < 3:
        exercise = input("What exercises would you like to do? (Enter one at a time): cardio, weight lifting, home workout\n")
        if exercise.lower() in options:
            if exercise not in exercises:
                exercises.append(exercise)
        else:
            print("Invalid input. Please choose from the options: cardio, weight lifting, home workout.")
            continue
        if len(exercises) < 3:
            more_exercises = input("Would you like to add any other exercises? (yes or no)\n")
            if more_exercises.lower() == "no":
                break
            elif more_exercises.lower() == "yes":
                print("Here are the exercises you can still choose from: ")
                for option in options:
                    if option not in exercises:
                        print(option)
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
                continue
    if len(exercises) == 3:
        print("You've chosen all the exercises.")
    print(f"You've chosen the following exercises: {', '.join(exercises)}")

# this asks the user what workouts he would like to do.
get_workout_plan()


