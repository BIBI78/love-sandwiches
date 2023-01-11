import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint



def weight_loss(weight, desired_weight, deficit_per_day):
    weight_loss_rate = weight - desired_weight
    deficit_needed = weight_loss_rate * 7700
    days_needed = deficit_needed / deficit_per_day
    return days_needed

def weight_gain(weight, height, age, target_weight):
    # Your code here to calculate time to reach target weight
    pass

def choose_weight_goal():
    goal = ""
    while goal != "gain" and goal != "lose":
        goal = input("Would you like to gain or lose weight? (gain/lose) ").lower()
    if goal == 'gain':
        weight_gain(weight, height, age, target_weight)
    else:
        weight_loss_time(weight, height, age, target_weight)
        weight = float(input("Enter your current weight in kg: "))
        target_weight = float(input("Enter your desired weight in kg: "))
        deficit_per_day = int(input("Enter your estimated calorie deficit per day: "))
        time = weight_loss_time(weight, target_weight, deficit_per_day)
        print(f"It will take approximately {time} days to reach your desired weight")




