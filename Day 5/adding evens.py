total=0
for n in range (1,101):
    if n%2==0:
        total+=n

print(total)

#or
t=0
for n in range(2,101,2):
    t+=n
print(t)