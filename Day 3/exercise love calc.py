print("Welcome to the Love Calc!!")
name1=input("enter your name.")
name2= input("what is his/her name? _")
#lower(), count(letter)
combined_string = name1+name2
lower_case=combined_string.lower()
t=lower_case.count("t")
r=lower_case.count("r")
u=lower_case.count("u")
e=lower_case.count("e")
l=lower_case.count("l")
o=lower_case.count("o")
v=lower_case.count("v")

ten_place= t+r+u+e
one_place=l+o+v+e
Love_Score = str(ten_place)+str(one_place)
if Love_Score<10 or Love_Score>90:
    print(f"your Love score is {Love_Score}%, you go together like coke and mentos")
elif Love_Score>=40 and Love_Score<=50:
    print(f"your Love score is {Love_Score}%,you are alright together")
else:
    print(f"your Love score is {Love_Score}%")