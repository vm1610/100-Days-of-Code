print("Welcome to python pizza deliveries!!")
size=input("what size pizza do u want? S, M, L")
add_pepperoni = input("Do u want pepperoni?   Y, N?")
extra_cheese = input("dO U WANT EXTRA CHEESE? Y,N?")
bill=0
if size == "S":
    bill=15
    if add_pepperoni == "Y":
        bill+=2

elif size == "M":
    bill=20
    if add_pepperoni == "Y":
        bill+=3
else:
    bill = 25
    if add_pepperoni == "Y":
        bill+=3
if extra_cheese=="Y":
    bll+=1
print(f"your final bill is : ${bill}")
