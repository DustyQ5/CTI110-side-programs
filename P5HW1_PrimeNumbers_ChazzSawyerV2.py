# input a number and the program will tell you if it is prime or not prime
# 11/08/2018
# CTI-110 P5HW1 - Prime Numbers
# Chazz Sawyer
#



# main function
def main():
    print('Hello, welcome to prime number checker.')
    number = int(input('What number would you like to check for prime status?'))
    print('This program will now check to see if',number,'is a prime number.')
    if isprime(number) == True:
        print(number,'is prime.')
    else:
        print(number,'is not prime.')
            

# is prime function
def isprime(number):
    if number <=1:#if number is 1 or less not prime
        return False
    elif number == 2:#manually insert 2 as prime number because loop wont say it is
        return True
    #any number divisible by five is not prime
    else:
        for five in range (2,number):
            if (five * 5) == number:
                return False
                break
            #loop checks for prime status
        else:
            for loop in range (2,number):
            
                if (number % loop) == 0:
                    return False
                    break
                else:
                    return True



main()

