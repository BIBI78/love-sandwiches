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

def workout_schedule():
    exercises = ['cardio', 'weight lifting', 'home exercise']
    options = {
        'cardio': ['treadmill', 'elliptical', 'stairmaster'],
        'weight lifting': ['bench press', 'squat', 'deadlift'],
        'home exercise': ['push-ups', 'crunches', 'lunges']
    }
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Prompt user for exercise type
    while True:
        exercise_choice = input(f"What type of exercise would you like to do? (Choose multiple): {exercises} ")
        chosen_exercises = [e.strip() for e in exercise_choice.split(",")]
        if all(e in exercises for e in chosen_exercises):
            break
        print("Invalid input, please choose again.")
    
    # Prompt user for exercise options
    chosen_options = []
    for exercise in chosen_exercises:
        while True:
            option_choice = input(f"What {exercise} exercise would you like to do? {options[exercise]} ")
            if option_choice in options[exercise]:
                chosen_options.append(option_choice)
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
                    exercise_choice = random.choice(chosen_options)
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


workout_schedule()