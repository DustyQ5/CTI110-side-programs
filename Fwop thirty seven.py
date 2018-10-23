import random
#global variable
fwop = 0

#repeats until fwop is thirty seven
def main():
    global fwop
    #was taking to long added optional 500 to end result after second resuls
    #to test if i could
    while fwop != 37 or fwop != 500:
        fwop = random.randint(1,10000)
        print(fwop)

main()
#first attempt with only 37 was completed in under a minute 
#took over thirty minutes did not find it a second time got bored
