#data types


#1strings

print("Hello"[0])
"Hello"[0]

print("123"+"345")


#2integer
print(123+345)

print(123_456_789)  #add commas''


#3float

3.1459


#boolean

True
False


###########################
#len(4838) error
# 

num_char=len(input("what is y0ur name?"))
#print("your name has"+num_char+"characters") error  
#change to str
new_num_char=str(num_char) 
print("your name has"+new_num_char+"characters")

#type()
print(type(num_char))

#changing data types

a=float(123)