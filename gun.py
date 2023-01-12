import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

def weight_loss_time(weight, desired_weight, deficit_per_day):
    weight_loss_rate = weight - desired_weight
    #this eqn is from the net
    deficit_needed = weight_loss_rate * 7700
    days_needed = deficit_needed / deficit_per_day
    return days_needed
"""
weight = float(input("Enter your current weight in kg: "))
desired_weight = float(input("Enter your desired weight in kg: "))
deficit_per_day = int(input("Enter your estimated calorie deficit per day: "))
time = weight_loss_time(weight, desired_weight, deficit_per_day)
print(f"It will take approximately {time} days to reach your desired weight")  

"""


def weight_gain_time(weight, height, age, desired_weight):
    # Harris-Benedict equation to calculate Basal Metabolic Rate (BMR)
    BMR = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    # Multiply BMR by 1.55 to estimate calorie intake needed to gain weight
    weight_gain_time = BMR * 1.55
    # Estimate time to reach desired weight (assuming a weight gain of 0.5 kg per week)
    time_to_reach_desired_weight = (desired_weight - weight) / 0.5
    return weight_gain_time, time_to_reach_desired_weight
"""
weight = float(input("Enter your current weight (in kg): "))
height = float(input("Enter your height (in cm): "))
age = int(input("Enter your age: "))
desired_weight = float(input("Enter your desired weight (in kg): "))

calories_per_day, time_to_reach_desired_weight = weight_gain_time(weight, height, age, desired_weight)
print("To gain weight, you should consume approximately", calories_per_day, "calories per day.")
print("It will take approximately {} weeks to reach your desired weight.".format(time_to_reach_desired_weight))

"""



def main():
    """
    trying to call all functions 
    """
   
# NEED A WAY TO CHOSE WICH ONE TO CALL 
# THE EQUATION IS A LITTLE FUCKED UP
# FUNCTION FOR EXERCISE 

weight = float(input("Enter your current weight (in kg): "))
height = float(input("Enter your height (in cm): "))
age = int(input("Enter your age: "))
desired_weight = float(input("Enter your desired weight (in kg): "))

calories_per_day, time_to_reach_desired_weight = weight_gain_time(weight, height, age, desired_weight)
print("To gain weight, you should consume approximately", calories_per_day, "calories per day.")
print("It will take approximately {} weeks to reach your desired weight.".format(time_to_reach_desired_weight))
 

main()

