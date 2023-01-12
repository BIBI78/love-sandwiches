import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint


"""
### edit this### this is the exercise function 
def exercise_suggestion(age, sex, weight, height, desired_weight):
    # Harris-Benedict equation to calculate Basal Metabolic Rate (BMR)
    BMR = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    # Multiply BMR by 1.55 to estimate calorie intake needed to gain weight
    calorie_intake = BMR * 1.55
    # Estimate time to reach desired weight (assuming a weight gain of 0.5 kg per week)
    time_to_reach_desired_weight = (desired_weight - weight) / 0.5
    #Calculate how much user should exercise per week
    exercise_calories = (calorie_intake - BMR)/7
    if sex == 'male':
        exercise_suggestion = exercise_calories/77
    else:
        exercise_suggestion = exercise_calories/88
    return exercise_suggestion

sex = input("Enter your sex (male or female): ")
age = int(input("Enter your age: "))
weight = float(input("Enter your current weight (in kg): "))
height = float(input("Enter your height (in cm): "))
desired_weight = float(input("Enter your desired weight (in kg): "))

exercise_per_week = exercise_suggestion(age, sex, weight, height, desired_weight)
print("You should exercise approximately {:.2f} hours per week.".format(exercise_per_week))

"""

def diet_suggestion(age, weight, height):
    # Harris-Benedict equation to calculate Basal Metabolic Rate (BMR)
    BMR = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    # Multiply BMR by 1.55 to estimate calorie intake needed to maintain weight
    calorie_intake = BMR * 1.55
    # Suggest diet based on age and calorie intake
    if age < 30:
        diet_suggestion = "Your suggested diet is {} calories per day with moderate exercise.".format(calorie_intake)
    elif 30 <= age < 60:
        diet_suggestion = "Your suggested diet is {} calories per day with regular exercise.".format(calorie_intake)
    else:
        diet_suggestion = "Your suggested diet is {} calories per day with regular exercise and a focus on nutrient-dense foods.".format(calorie_intake)
    return diet_suggestion

age = int(input("Enter your age: "))
weight = float(input("Enter your current weight (in kg): "))
height = float(input("Enter your height (in cm): "))

suggested_diet = diet_suggestion(age, weight, height)
print(suggested_diet)





