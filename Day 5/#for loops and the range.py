#for loops and the range
#for number in range(a,b,c): #c=step size
#   print(number)
for number in range (1,10,3): #not in;cluding 10
    print(number)
total=0#(accumulator)
for number in range(1,101):
    total+=number

print(total)