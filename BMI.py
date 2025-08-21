#Getting the necessary inputs
weight = float(input("Enter your weight in Kilograms: "))
height = float(input("Enter your height in meters: "))

#Input validating
if weight <=0 or height <=0:
    print("Wrong input, idiot")

#Calculating the weight (Fomula)
BMI = weight/(height**2)

#Printing the BMI
print(f"Your BMI is: {BMI:.2f}")

#Printing the output
if BMI <18.5:
    print("You are underweight")
elif 18.5 <= BMI <= 25:
    print("You're in the perfect fit")
else:
    print("You're overweight, go do exercise")
