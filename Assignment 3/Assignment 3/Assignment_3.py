
# Assignment 3
# this one seems to just be building off of Assignment 2 based on the wording

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


# start
print("Welcome to CJ's BMI Calculator")


# weight input
print("Enter your current Weight (lbs)")


try: 
    weight = float(input())
except ValueError: # checking to make sure it is a float. data type validation
    raise ValueError("Weight must be a valid number.")

if weight <= 0: # checking for range.. if you're 0 lbs you shouldn't be using this
    raise ValueError("Weight must be greater than 0 lbs.") # reponse

# height via feet input
print("Enter your current Height (ft)")

try: 
    feet = int(input())
except ValueError: # checking to make sure it is a float. data type validation
    raise ValueError("Height must be a valid number.")

if feet <= 0: # As long as it is not zero. data range validation
    raise ValueError("Height must be greater than 0 ft.")


# height via inch input
print("Enter your current Height (in)")

try: 
    inch = int(input())
except ValueError: # checking to make sure it is a float. data type validation
    raise ValueError("Height must be a valid number.")

if inch <= -1: # as long as this isn't negative, it is valid
    raise ValueError("Height must be greater than -1 in.")

# call processes
height = height_process(feet,inch)
bmi = bmi_process(weight,height)
report = report_process(bmi)

# ranges
print("BMI ranges provided by World Health Organization")
print("BMI of 18 or lower - Underweight")
print("BMI of 18.5 to 25 - Normal range")
print("BMI of 25.5 or higher - Overweight")

# report
print(f"With a BMI of {bmi:.1f}, you are {report}.")