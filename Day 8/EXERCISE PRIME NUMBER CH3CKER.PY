def prime_checker(number):
    is_prime=True
    if number==1:
        print("number is not a prime number")
    elif number>1:
        for i in range (2,number):
            if number%i==0:
                is_prime=False
        if is_prime:
            print("is a prime")
        else:
            print("not a prime")
def main():
    n = int(input("Check this number: "))
    prime_checker(number=n)
main()
