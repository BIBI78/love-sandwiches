import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

## JSAIS PAS ##
import requests
import json

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
"""


"""
def food_group_suggestion(preference):
    # Suggest a food group based on user preference
    if preference == 'vegetarian':
        food_group_suggestion = 'Plant-based foods'
    elif preference == 'low-carb':
        food_group_suggestion = 'Protein and healthy fats'
    elif preference == 'high-protein':
        food_group_suggestion = 'Lean meats, eggs, and dairy'
    else:
        food_group_suggestion = 'A balanced mix of all food groups'
    return food_group_suggestion

preference = input("Enter your dietary preference (vegetarian, low-carb, high-protein, or none): ")

suggested_food_group = food_group_suggestion(preference)
print("Your suggested food group is: {}.".format(suggested_food_group))
"""
"""
### THIS IS THE DIET CODE ###
# ok the first part works but i would like the FOOD group suggestion part to work too,
# nested if statement ??
def ask_question(question, valid_responses):
    while True:
        response = input(question)
        if response in valid_responses:
            if response == 'veg':
                food_group_suggestion = 'Plant-based foods'
            elif response == 'protein':
                food_group_suggestion = 'eggs , lean meat, dairy'
            elif response == 'carb':
                food_group_suggestion = 'Protein and healthy fats'
            elif response == 'none':
                food_group_suggestion = 'A balanced mix of all food groups'
            return response
        else:
            print("Invalid response, please enter one of the following: {}".format(valid_responses))

question = "Enter your dietary preference (vegetarian, low-carb, high-protein, or none): "
valid_responses = ["a", "b", "c", "d"]

#suggested_food_group = food_group_suggestion(response)
answer = ask_question(question, valid_responses)
print("Your answer is: {}".format(answer))

"""




## neeed an api key ##
def get_weather(api_key, city_name):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    weather_data = json.loads(response.text)
    if 'cod' not in weather_data or weather_data['cod'] != 200:
        return None
    else:
        return weather_data

api_key = "YOUR_API_KEY"
city_name = "london"
weather = get_weather(api_key, city_name)

if weather is None:
    print("Unable to get the weather for the given city")
else:
    print("Temperature in {} is {} degree celcius".format(city_name, weather['main']['temp']))




    ####

     #3

# ok the first part works but i would like the FOOD group suggestion part to work too,
# nested if statement ??
def ask_question(question, valid_responses):
    while True:
        response = input(question)
        if response in valid_responses:
            if response == 'a':
                food_group_suggestion = 'Plant-based foods'
            elif response == 'protein':
                food_group_suggestion = 'eggs , lean meat, dairy'
            elif response == 'carb':
                food_group_suggestion = 'Protein and healthy fats'
            elif response == 'none':
                food_group_suggestion = 'A balanced mix of all food groups'
            return response
        else:
            print("Invalid response, please enter one of the following: {}".format(valid_responses))

question = "Enter your dietary preference (vegetarian, low-carb, high-protein, or none): "
valid_responses = ["a", "b", "c", "d"]

#suggested_food_group = food_group_suggestion(response)
answer = ask_question(question, valid_responses)
print("Your answer is: {}".format(answer))

####