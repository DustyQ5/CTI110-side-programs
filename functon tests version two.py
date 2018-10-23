#added next line late to test global variable change
fwop_global = 456
FWOP_GLOBAL_CONSTANT = 6
# this is a mess
def main():
    test_function_variable()
    fwop = input('What is fwop?')
    print(fwop)
   
    fwop_value = float(input('If Fwop was a number what number would Fwop be?')) 
    fwop_play(fwop_value)
    fwop_one = float(input('I need a Fwopping number.'))
    fwop_two = float(input('I need another Fwopping number.'))
    fwop_multi(fwop_one, fwop_two)
    fwop_keywords_test(varx=0.256,varq=5,varz=17,vary=7)
    print(fwop_global)
    fwop_global_change()
    print(fwop_global)
    
def test_function_variable():
    print('Happy, happy EXPLOSION!')
    
def fwop_play(number):
    fwop_result = number * 2 /8 + 3
    print(fwop_result)

def fwop_multi(one,two):
    result = one * two
    print(result)

# Mo complicates because keyword arguments.
def fwop_keywords_test(varx,vary,varz,varq):
    over_complication = varx + varq * varz / vary /varz + varx +vary + varq + varz
    print(over_complication)

#this changes a global variable
def fwop_global_change():
    global fwop_global
    fwop_global = fwop_global * 3
    fwop_constant = 45 * FWOP_GLOBAL_CONSTANT
    print(fwop_constant)




main()
