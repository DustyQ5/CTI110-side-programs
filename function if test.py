def main():
    print('This tests if else statements and function')
    number_test = float(input('Please insert a number'))
    if number_tester(number_test):
        print('This number is five.')
    else:
        print('This number is not five.')



def number_tester(number_test):
    if (number_test) == 5:
        status = True
    else:
        status = False
    return status

main()
