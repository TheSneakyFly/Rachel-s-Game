import time

yes = ['yes','y']
no = ['no','n']
answers = ['yes','y','no','n']
level = 1

def pause(seconds=.7):
    time.sleep(seconds)

def question(string):
    inp="none"
    while inp.lower() not in answers:
        print (string)
        inp=input(">")
        if inp.lower() in yes:
            answer=True
        elif inp.lower() in no:
            answer=False
        else:
            print("\nPlease enter Yes or No")
    return answer

def try_again():
    inp="none"
    while inp.lower() not in answers:
        print('\nWould you like to try again? (y or n) ')
        pause()
        inp= input()
        if inp.lower() in yes:
            return True
        if inp.lower() in no:
            return False
        else:
            print('\nYes or No!')
            pause()

def high_low(number,close_range=5):
    g=0
    while g != number:
        try:
            g=int(input("\n>"))
        except:
            print("\nThat's not a number! Quit? (y/n) ")
            quit = 0
            while quit not in answers:
                quit = input(">")
                if quit in yes:
                    return False
                if quit in no:
                    continue
                else:
                    print('\nQuit? (y/n)')
        if g == number:
            return True
        if g in range(number-close_range,number):
            print('A bit higher')
        if g in range(number+1,number+close_range):
            print('A bit lower')
        elif g < number-close_range:
            print('Guess higher')
        elif g > number:
            print('Guess lower')

answer1 = False
while answer1 == False:
    answer1 = question('\nAre you Rachel?')
    if answer1 == True:
        print('\nCongratulations you are beautiful!')
        pause(1.2)
        level += 1
        answer2 = True
        while answer2 == True:
            answer2 = question('\nAre you hungry? ')
            if answer2 == True:
                print('\nOh god... ')
                pause()
                print('.....')
                pause()
                print("\nPlease don't hurt me!")
                print("*Manny runs in fear for his life*")
                pause(2)
                if try_again() == False:
                    break
            if answer2 == False:
                print("\nOkay good!, Let's continue! :D ")
                pause()
                print("...")
                pause(1.5)
                print('\nBut first,')
                pause()
                print('\nI do have to make sure you are the "real" Rachel,')
                print('this is a very sensitive matter, afterall...')
                pause(3)
                level += 1
                answer3 = "none"
                fav_color = ["purple","2"]
                color_options = ["(1)Red ","(2)Purple ","(3)Pink ","(4)Orange"]
                colors = ['1','2','3','4','red','purple','pink','orange']
                while answer3 not in fav_color:
                    print('\n\nWhat is your favorite color? (Type the color or number)')
                    print(*color_options)
                    answer3 = input('')
                    pause()
                    if answer3.lower() not in colors:
                        print("\nThat's not even an option!!")
                        pause()
                        if try_again() == False:
                            break
                    if str(answer3.lower()) not in fav_color:
                        print('\nI knew you were an imposter!!')
                        pause()
                        if try_again() == False:
                            break
                    if str(answer3.lower()) in fav_color:
                        print('\nWow you really know your stuff!')
                        pause(1)
                        level += 1
                        answer4 = 0
                        while answer4 == 0:
                            print("\n\nhmmmm...")
                            pause(2)
                            print("\nAHAA!")
                            pause()
                            print("\nOnly the real Rachel would know what year she was born.")
                            pause(2)
                            print("What year would you say that was exactly?..")
                            pause(2)
                            answer4 = high_low(1995)
                            if answer4 == True:
                                answer=1
                                print("\nYou made it!")
                            if answer4 == False:
                                break



    if answer1 == False:
        print('\nYou are probably ugly')
        pause()
        print('\n..sorry')
        pause()
        print('\nGoodbye!')
        pause(1.5)
        if try_again() == False:
            break



pause()
print('\n\n-------------------')
print("\nYou made it to level " + str(level) + ". Congrats!")
input('\nPress enter to exit!')
