import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint


def choose_weight_goal():
    goal = ""
    while goal != "gain" and goal != "lose":
        goal = input("Would you like to gain or lose weight? (gain/lose) ").lower()
    weight = float(input("What is your weight in pounds? "))
    height = float(input("What is your height in inches? "))
    age = float(input("What is your age in years? "))
    target_weight = float(input("What is your target weight in pounds? "))
    if goal == 'gain':
        weight_gain(weight, height, age, target_weight)
    else:
        weight_loss(weight, height, age, target_weight)


def weight_loss(weight, desired_weight, deficit_per_day):
    weight_loss_rate = weight - desired_weight
    deficit_needed = weight_loss_rate * 7700
    days_needed = deficit_needed / deficit_per_day
    return days_needed

weight = float(input("Enter your current weight in kg: "))
desired_weight = float(input("Enter your desired weight in kg: "))
deficit_per_day = int(input("Enter your estimated calorie deficit per day: "))
time = weight_loss(weight, desired_weight, deficit_per_day)
print(f"It will take approximately {time} days to reach your desired weight")  

    


def weight_gain(weight, height, age, target_weight):
    # Calculate the user's current BMI
    bmi = weight / (height ** 2)
    
    # Assume a healthy BMI range
    if bmi < 18.5:
        print("You are underweight.")
    elif bmi >= 18.5 and bmi <= 24.9:
        print("You have a normal weight.")
    else:
        print("You are overweight.")
    
    # Estimate the number of weeks it will take to reach target weight
    target_weight_diff = target_weight - weight
    # 3500 calories in a pound
    target_calorie_diff = target_weight_diff * 3500
    # Assume user needs to consume an additional 500 calories per day
    target_days = target_calorie_diff / 500
    weeks = target_days / 7
    
    return weeks

weight = float(input("What is your weight in pounds? "))
height = float(input("What is your height in inches? "))
age = float(input("What is your age in years? "))
target_weight = float(input("What is your target weight in pounds? "))
weeks = weight_gain(weight, height, age, target_weight)
print("It will take approximately", weeks, "weeks to reach your target weight.")

###
def weight_loss_time(weight, desired_weight, deficit_per_day):
    weight_loss_rate = weight - desired_weight
    #this eqn is from the net
    deficit_needed = weight_loss_rate * 7700
    days_needed = deficit_needed / deficit_per_day
    return days_needed

weight = float(input("Enter your current weight in kg: "))
desired_weight = float(input("Enter your desired weight in kg: "))
deficit_per_day = int(input("Enter your estimated calorie deficit per day: "))
time = weight_loss_time(weight, desired_weight, deficit_per_day)
print(f"It will take approximately {time} days to reach your desired weight")  


# new goal

    def choose_weight_goal():
    goal = ""
    while goal != "gain" and goal != "lose":
        goal = input("Would you like to gain or lose weight? (gain/lose) ").lower()
    weight = float(input("What is your weight in pounds? "))
    height = float(input("What is your height in inches? "))
    age = float(input("What is your age in years? "))
    target_weight = float(input("What is your target weight in pounds? "))
    if goal == 'gain':
        weight_gain(weight, height, age, target_weight)
    else:
        weight_loss(weight, height, age, target_weight)


        #### lastest attemopt
        def weight_gain(weight, height, age, target_weight):
    # Calculate the user's current BMI
    bmi = weight / (height ** 2)
    
    # Assume a healthy BMI range
    if bmi < 18.5:
        print("You are underweight.")
    elif bmi >= 18.5 and bmi <= 24.9:
        print("You have a normal weight.")
    else:
        print("You are overweight.")
    
    # Estimate the number of weeks it will take to reach target weight
    target_weight_diff = target_weight - weight
    # 3500 calories in a pound
    target_calorie_diff = target_weight_diff * 3500
    # Assume user needs to consume an additional 500 calories per day
    target_days = target_calorie_diff / 500
    weeks = target_days / 7
    
    return weeks

def weight_loss(weight, desired_weight, deficit_per_day):
    weight_loss_rate = weight - desired_weight
    #this eqn is from the net
    deficit_needed = weight_loss_rate * 7700
    days_needed = deficit_needed / deficit_per_day
    return days_needed


























def choose_weight_goal():
    goal = ""
    while goal != "gain" and goal != "lose":
        goal = input ("Would you like to gain or lose some weight? (gain or lose)").lower
    weight = float(input("What is your weight in kg? "))
    height = float(input("What is your height in cm? "))
    age = float(input("What is your age in years? "))
    target_weight = float(input("What is your target weight in kg? "))
    if goal == 'gain':
        weight_gain(weight, height, age, target_weight)
    else:
        weight_loss(weight, height, age, target_weight)


    choose_weight_goal(weight, height, age, target_weight)
        


#########
def calorie_intake(weight, height, age, desired_weight):
    # Harris-Benedict equation to calculate Basal Metabolic Rate (BMR)
    BMR = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    # Multiply BMR by 1.55 to estimate calorie intake needed to gain weight
    calorie_intake = BMR * 1.55
    time_to_reach_desired_weight = (desired_weight - weight) / 0.5
    return calorie_intake, time_to_reach_desired_weight

weight = float(input("Enter your current weight (in kg): "))
height = float(input("Enter your height (in cm): "))
age = int(input("Enter your age: "))
desired_weight = float(input("Enter your desired weight (in kg): "))


calories_per_day, time_to_reach_desired_weight = calorie_intake(weight, height, age, desired_weight)

calories_per_day = calorie_intake(weight, height, age, desired_weight)
print("To gain weight, you should consume approximately", calories_per_day, "calories per day.")