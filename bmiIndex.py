

# Calculating body mass index

print("Want to calculate your Body Mass Index (BMI)?")

# Get height in feet and inches
feet = float(input("Enter your height (feet): "))
inches = float(input("Enter your height (inches): "))

# Convert height to meters (1 foot = 0.3048 meters, 1 inch = 0.0254 meters)
heightm = (feet * 0.3048) + (inches * 0.0254)

# Get weight in pounds
weightlbs = float(input("Enter your weight in pounds (lbs): "))

# Convert weight to kilograms (1 pound = 0.453592 kilograms)
weightkg = weightlbs * 0.453592

# Calculate BMI
result = weightkg / (heightm ** 2)
print(f"Your BMI is: {result:.2f}")


# BMI categories
if result < 18.5:
    print("You are underweight.")
elif 18.5 <= result < 25:
    print("You are normal weight.")
elif 25 <= result < 30:
    print("You are slightly overweight.")
elif 30 <= result < 35:
    print("You are obese.")
else:
    print("You are clinically obese.")

