#nested if/else condition
#If condition:
    #do this
    #If condition:
        #do this
    #elif:
        #do this
    #elif:
        #do this
    #elif:
        #do thiS
    #.
    #...
    #else:
        #do this
#else:
    #do this
Height = int(input("ENTER YOUR HEIGHT IN CM? "))
age=int(input("enter your age."))
if Height>=120:
    print("You can ride the rollercoaster")
    if age <12:
        print("please pay $5")
    elif age <=18 :
        print("please pay $7")
    else:
        print("please pay $12")
        
else:
    print("You can not ride the rollercoaster!!")

