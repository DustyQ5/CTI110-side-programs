def main():
    rocka = 0
    while rocka ==0:
        number = int(input('NUMBER'))
        if isprime(number) == True:
            print(number,'is prime')
        else:
            print(number,'is not prime')


def isprime(number):
    if number <=1:
        return False
    elif number == 2:#manually insert 2 as prime number
        return True




    
    # this needs to check to see if a number is divisible by five
    #and then return false
    else:
        for five in range (2,number,5):
            if (number % five) == 0:
                return False
                break






        
        else:#loop starts atleast at 2 or everything is not prime
            for loop in range (2,number):
            # switch number and loop and everything is prime
                if (number % loop) == 0:
                    return False
                    break
                else:
                    return True



main()
               
# works but also says anything ending in a 5 is prime
# 5 is only legal prime number because all other numbers ending in
# 5 are divisible by five
