import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint


def weight_gain_time(weight, height, age, desired_weight):
    # Harris-Benedict equation to calculate Basal Metabolic Rate (BMR)
    BMR = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    # Multiply BMR by 1.55 to estimate calorie intake needed to gain weight
    weight_gain_time = BMR * 1.55
    # Estimate time to reach desired weight (assuming a weight gain of 0.5 kg per week)
    time_to_reach_desired_weight = (desired_weight - weight) / 0.5
    return weight_gain_time, time_to_reach_desired_weight

weight = float(input("Enter your current weight (in kg): "))
height = float(input("Enter your height (in cm): "))
age = int(input("Enter your age: "))
desired_weight = float(input("Enter your desired weight (in kg): "))

calories_per_day, time_to_reach_desired_weight = weight_gain_time(weight, height, age, desired_weight)
print("To gain weight, you should consume approximately", calories_per_day, "calories per day.")
print("It will take approximately {} weeks to reach your desired weight.".format(time_to_reach_desired_weight))
