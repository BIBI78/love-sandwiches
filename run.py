import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')


def get_sales_data():
    """
    Get sales figures input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 6 numbers separated
    by commas. The loop will repeatedly request data, until it is valid.
    """
    while True:
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Enter your data here:\n ")

        sales_data = data_str.split(",")

        if validate_data(sales_data):
            print("Data is valid!")
            break

    return sales_data


def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def update_worksheet(data, worksheet):
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")


def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus for each item type.
    The surplus is defined as the sales figure subtracted from the stock:
    - Positive surplus indicates waste
    - Negative surplus indicates extra made when stock was sold out.
    """
    print("Calculating surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    
    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)

    return surplus_data


def get_last_5_entries_sales():
    """
    Collects columns of data from sales worksheet, collecting
    the last 5 entries for each sandwich and returns the data
    as a list of lists.
    """
    sales = SHEET.worksheet("sales")
    # column = sales.col_values(3)
    # print(column)

    columns = []
    for ind in range(1,7):
        column = sales.col_values(ind)
        columns.append(column[-5:])

    return columns 






def main():
    """
    Run all program functions
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_worksheet(sales_data, "sales")
    new_surplus_data = calculate_surplus_data(sales_data)
    update_worksheet(new_surplus_data, "surplus")
    sales_column = get_last_5_entries_sales()
    stock_data = calculate_stock_data(sales_column)
    update_worksheet(stock_data,"stock")




#print("Welcome to Love Sandwiches Data Automation")
#main()







 


#get_username()





def encrypt_name():
    name = input("What is your name? ")
    new_name = ""
    for i in name:
        new_name += chr(ord(i) + 66)
        print(new_name)

    return new_name

print(encrypt_name())



# this code illl use to generate user name
def name_66():
    name = input("What is your name? ")
    new_name66 = name + "66"
    print(new_name66)

    return new_name66

##print(name_66())


#def calorie_intake(weight, age, height):
    #BMR = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    #return BMR
#weight = float(input("Enter your weight in kg: "))
#age = int(input("Enter your age in years: "))
#height = float(input("Enter your height in cm: "))
#intake = calorie_intake(weight, age, height)
#print("Your recommended daily calorie intake is: ", intake)




def weight_loss_time(weight, desired_weight, deficit_per_day):
    weight_loss_rate = weight - desired_weight
    deficit_needed = weight_loss_rate * 7700
    days_needed = deficit_needed / deficit_per_day
    return days_needed

weight = float(input("Enter your current weight in kg: "))
desired_weight = float(input("Enter your desired weight in kg: "))
deficit_per_day = int(input("Enter your estimated calorie deficit per day: "))
time = weight_loss_time(weight, desired_weight, deficit_per_day)
print(f"It will take approximately {time} days to reach your desired weight")



def weight_gain_time(weight, height, age, target_weight):
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
weeks = weight_gain_time(weight, height, age, target_weight)
print("It will take approximately", weeks, "weeks to reach your target weight.")



######
def weekly_schedule():
  # List of exercise options
  exercise_options = ["running", "weightlifting", "yoga", "swimming", "cycling", "boxing"]
  print("running", "weightlifting", "yoga", "swimming", "cycling", "boxing")
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


weekly_schedule()