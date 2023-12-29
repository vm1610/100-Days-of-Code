''' def my_function():'''
def greet():
    print("hello")
    print("how do u do?")
    print("Isn't the weather nice today?")


#FUNCTION THAT ALLOWS FOR INPUT
def greet_w_name(name): #paramater)
    print(f"Hello {name}\nHow do you do {name}?\nIsn't the weaather nice today?")
#greet_w_name("Vasu")v #argument

#multiple inputs
def greet_with(name,location):
    print(f"Hello {name}\nHow is it like in {location}")
greet_with("Vasu","Nowhere")
greet_with(name="Vasu",location="Nowhere")
#keyword arguments
#def my_function(a,b,c):
    #my_function(b=1,a=2,c=3)    