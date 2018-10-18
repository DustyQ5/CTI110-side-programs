
def main():
    test_function_variable()
    fwop = input('What is fwop?')
    print(fwop)
    fwop_value = float(input('If Fwop was a number what number would Fwop be?')) 
    fwop_play(fwop_value)
    fwop_one = float(input('I need a Fwopping number.'))
    fwop_two = float(input('I need another Fwopping number.'))
    fwop_multi(fwop_one, fwop_two)
  
    
    
def test_function_variable():
    print('Happy, happy EXPLOSION!')
    
def fwop_play(number):
    fwop_result = number * 2 /8 + 3
    print(fwop_result)

def fwop_multi(one,two):
    result = one * two
    print(result)








main()
