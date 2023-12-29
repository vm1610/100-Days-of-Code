h = float(input("enter your height in m: "))
w = int(input("enter your weight in kgs: "))
bmi = int(w)/float(h)**2
print(f"your bmi is {bmi} you are...")
if bmi <18.5:
    print("underweight")
elif bmi<25:
    print("normal weeight")
elif  bmi<30:
    print("overweight")
elif bmi<35:
    print("obese")
else:
    print("clinially obese")
