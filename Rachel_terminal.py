import time

inp='none'
inp2='none'
yes=['yes','y']
no=['no','n']
answers=['yes','y','no','n']

while inp.lower() not in yes:
    inp=input('\nAre you Rachel? ')
    if inp.lower() in yes:
        print('\nCongratulations you are beautiful!')
        time.sleep(1)
        while inp2.lower() not in no:
            inp2=input('\nAre you hungry? ')
            if inp2.lower() in yes:
                print('\nOh god... ')
                time.sleep(1)
                print('.....')
                time.sleep(1)
                print("\nPlease don't hurt me!")
                print("*Manny runs in fear for his life*")
            elif inp2.lower() in no:
                print("\nOkay good!, Let's continue! :D ")
            else:
                print("\nYes or no only please!.. I don't need your life story")
    elif inp.lower() in no:
        print('\nYou are probably ugly')
        time.sleep(1)
        print('\n..sorry')
        time.sleep(1)
        print('\nGoodbye!')
        time.sleep(.5)
    else:
        print('\nPlease answer yes or no!')

time.sleep(1)
input('\n\nPress enter to exit!')
