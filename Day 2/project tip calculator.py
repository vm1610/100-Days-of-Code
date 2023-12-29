print("Welcome to the tip calculator")
a =float(input("What was the total bill? $" ))
b=int(input("how many perceentage tip do you want to give? 10,12 or 15? "))
c=int(input("how many people are splitting the bill? "))

t = (a)+(b)*(a)/100
s= round(t/(c),2)

print(f"each person should pay: ${s}")