# Assignment 4
# this one seems to just be building off of Assignment 2 and 3 based on the wording

# functions that are related to processing different variables
def height_process(feet, inch):
    height = (feet * 12) + inch
    print(f"Total height: {height} inches")
    return height

def bmi_process(weight,height):
    bmi = (weight/height** 2) * 703
    print(f"BMI: {bmi:.1f}")
    return bmi

def report_process(bmi):
    # output
    if (bmi <= 18): 
        return "Underweight"
    elif(bmi >= 25.5): # this should be my nested if acting as the else if
        return "Overweight"
    else:
        return "within the normal range"

# BMI ranges provided by https://www.who.int/data/gho/data/themes/topics/topic-details/GHO/body-mass-index

def bmi_table():
    # BMI table
    print("                                             BMI Table") # I wanted to do some fancy formatting here
    print("Weight/Height", end="")

    # height columns
    for height in range(58, 77, 2): # start value, end +1, inc
        print(f"{height:8}", end="")
    print()

    # weight rows
    for weight in range(100, 251, 10): # start value, end +1, inc
        print(f"{weight:12}", end="")

        for height in range(58, 78, 2): # start value, end +1, inc
            bmi = (weight / height ** 2) * 703
            print(f"{bmi:8.1f}", end="")

        print()

# start

running = 1

# this is the main loop
while running == 1:
    valid = 0

    print("Welcome to CJ's BMI Calculator")

    # weight 
    while valid == 0:   
        print("Enter your current Weight (lbs)")
        try: 
            weight = float(input())
            if weight <= 0: # checking for range.. if you're 0 lbs you shouldn't be using this
                print("Weight must be greater than 0 lbs.") # reponse
            else: # this is for correctly inputing
                valid = 1
        except ValueError: # checking to make sure it is a float. data type validation
            print("Weight must be a valid number.")  


    # height via feet input 
    valid = 0
    while valid == 0:   
        print("Enter your current Height (ft)")
        try: 
            feet = float(input())
            if feet <= 0: # checking for range.. if you're 0 lbs you shouldn't be using this
                print("Height must be greater than 0 ft.") # reponse
            else: # this is for correctly inputing
                valid = 1
        except ValueError: # checking to make sure it is a float. data type validation
            print("Height must be a valid number.")  



    # height via inch input
    valid = 0
    while valid == 0:   
        print("Enter your current Height (in)")
        try: 
            inch = float(input())
            if inch < 0: # checking for range
                print("Height must be 0 or greater.") # reponse
            else: # this is for correctly inputing
                valid = 1
        except ValueError: # checking to make sure it is a float. data type validation
            print("Height must be a valid number.")  

    # call processes
    height = height_process(feet,inch)
    bmi = bmi_process(weight,height)
    report = report_process(bmi)

    # ranges
    print("BMI ranges provided by World Health Organization")
    print("BMI of 18 or lower - Underweight")
    print("BMI of 18.5 to 25 - Normal range")
    print("BMI of 25.5 or higher - Overweight")

    bmi_table()

    # report
    print(f"With a BMI of {bmi:.1f}, you are {report}.")

    # loop
    valid = 0
    while valid == 0:
        print("Would you like to run the Program again?")
        print("1. Yes")
        print("2. No")

        try:
            choice = float(input())
            if choice == 1:
                running = 1
                valid = 1
            elif choice == 2:
                print("Connection terminated.")
                running = 0
            else:
                print("Invalid selection, please try again.")
        except ValueError:
            print("Invalid selection, please try again.")

