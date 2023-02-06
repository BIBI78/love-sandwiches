import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint


# Function 1
#weight loss function

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

#3
"""
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




def main():
    """
    trying to call all functions 
    """



#1
"""
weight = float(input("Enter your current weight in kg: "))
desired_weight = float(input("Enter your desired weight in kg: "))
deficit_per_day = int(input("Enter your estimated calorie deficit per day: "))
time = weight_loss_time(weight, desired_weight, deficit_per_day)
print(f"It will take approximately {time} days to reach your desired weight")  
"""

#2
"""
# FUNCTION 2
# NEED A WAY TO CHOSE WICH ONE TO CALL 
# THE EQUATION IS A LITTLE FUCKED UP
# FUNCTION FOR EXERCISE 
# FUnction for  gain weight 
weight = float(input("Enter your current weight (in kg): "))
height = float(input("Enter your height (in cm): "))
age = int(input("Enter your age: "))
desired_weight = float(input("Enter your desired weight (in kg): "))

calories_per_day, time_to_reach_desired_weight = weight_gain_time(weight, height, age, desired_weight)
print("To gain weight, you should consume approximately", calories_per_day, "calories per day.")
print("It will take approximately {} weeks to reach your desired weight.".format(time_to_reach_desired_weight))
 """


 #3
"""
# ok the first part works but i would like the FOOD group suggestion part to work too,
# nested if statement ??
def ask_question(question, valid_responses):
    while True:
        response = input(question)
        if response in valid_responses:
            if response == 'a':
                print('Plant-based foods')
            elif response == 'b':
                print('eggs , lean meat, dairy')
            elif response == 'c':
                print('Protein and healthy fats')
            elif response == 'd':
                print('A balanced mix of all food groups')
            return response
        else:
            print("Invalid response, please enter one of the following: {}".format(valid_responses))

question = "Enter your dietary preference (vegetarian, low-carb, high-protein, or none): "
valid_responses = ["a", "b", "c", "d"]

#suggested_food_group = food_group_suggestion(response)
answer = ask_question(question, valid_responses)
# delete this
print("Your answer is: {}".format(answer))


"""
#FUNCTION 5
"""
### ADD TRY EXCEPT BS###
def weight_change():
    while True:
        weight_change = input("Would you like to lose or gain weight? (lose or gain): ")
        if weight_change == "lose":
            weight = float(input("Enter your current weight in kg: "))
            desired_weight = float(input("Enter your desired weight in kg: "))
            deficit_per_day = int(input("Enter your estimated calorie deficit per day: "))
            time = weight_loss_time(weight, desired_weight, deficit_per_day) 
            print(f"It will take approximately {time} days to reach your desired weight") 
            weight_loss_time(weight, desired_weight, deficit_per_day)
            break
        elif weight_change == "gain":
            weight = float(input("Enter your current weight (in kg): "))
            height = float(input("Enter your height (in cm): "))
            age = int(input("Enter your age: "))
            desired_weight = float(input("Enter your desired weight (in kg): "))
            calories_per_day, time_to_reach_desired_weight = weight_gain_time(weight, height, age, desired_weight)
            print("To gain weight, you should consume approximately", calories_per_day, "calories per day.")
            print("It will take approximately {} weeks to reach your desired weight.".format(time_to_reach_desired_weight))
            weight_gain_time(weight, height, age, desired_weight)
            break
        else:
            print("Invalid response, please enter either 'lose' or 'gain'")

def weight_loss_time(weight, desired_weight, deficit_per_day):
    weight_loss_rate = weight - desired_weight
    #this eqn is from the net
    deficit_needed = weight_loss_rate * 7700
    days_needed = deficit_needed / deficit_per_day
    return days_needed

def weight_gain_time(weight, height, age, desired_weight):
    # Harris-Benedict equation to calculate Basal Metabolic Rate (BMR)
    BMR = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    # Multiply BMR by 1.55 to estimate calorie intake needed to gain weight
    weight_gain_time = BMR * 1.55
    # Estimate time to reach desired weight (assuming a weight gain of 0.5 kg per week)
    time_to_reach_desired_weight = (desired_weight - weight) / 0.5
    return weight_gain_time, time_to_reach_desired_weight



weight_change()




"""

main()


    