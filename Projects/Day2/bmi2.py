from time import sleep

#BMI CALCULATOR WITH CATEGORIES
print("Welcome to BMI Calculator")
sleep(3)
print("""
      Underweight: BMI < 18.5
      Normal weight: 18.5 <= BMI < 24.9
      Overweight: 25 <= BMI < 29.9
      Obese: BMI >= 30
      """)

height = float(input("Please enter your height: "))
weight = float(input("Enter your weight: "))

bmi = weight/height**2
sleep(2)
print("BMI CATEGORY")
if bmi < 18.5:
    print(f"Your BMI is {bmi:.2f}, your are underweight")
elif 18.5 <= bmi < 24.9:
    print(f"Your BMI is {bmi:.2f}, your have a normal weight")
elif 25 <= bmi < 30:
    print(f"Your BMI is {bmi:.2f}, your are overweight")
else:
    print(f"Your BMI is {bmi:.2f}, you are obese")