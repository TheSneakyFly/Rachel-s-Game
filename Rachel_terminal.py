import time

yes = ['yes','y']
no = ['no','n']
answers = ['yes','y','no','n']

def pause(seconds=.7):
    time.sleep(seconds)

def question(string):
    inp="none"
    while inp.lower() not in answers:
        print (string)
        inp=input("")
        if inp.lower() in yes:
            answer=True
        elif inp.lower() in no:
            answer=False
        else:
            print("\nPlease enter Yes or No")
    return answer

answer1 = False
while answer1 == False:
    answer1 = question('\nAre you Rachel?')
    if answer1 == True:
        print('\nCongratulations you are beautiful!')
        pause(1.2)
    elif answer1 == False:
        print('\nYou are probably ugly')
        pause()
        print('\n..sorry')
        pause()
        print('\nGoodbye!')
        pause(1.5)

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
    if answer2 == False:
        print("\nOkay good!, Let's continue! :D ")
        pause(2)
        print("...")
        pause(2)
        print('\nBut first')
        pause(1)
        print('...')
        pause(1)
        print('\nI do have to make sure you are the "real" Rachel,')
        pause(2)
        print('this is a very sensitive matter, afterall')
        pause(2.5)

answer3 = "none"
fav_color = ["purple","2"]
color_options = ["(1)Red ","(2)Purple ","(3)Pink ","(4)Orange"]
colors = ['1','2','3','4','red','purple','pink','orange']
while answer3 not in fav_color:
    print('\n\nWhat is your favorite color? (Type the color or number)')
    print(*color_options)
    answer3 = input('')
    pause()
    if str(answer3.lower()) in fav_color:
        print('\nWow you really know your stuff!')
        pause()
    if answer3.lower() not in colors:
        print("\nThat's not even an option!!")
        pause()
    elif str(answer3.lower()) not in fav_color:
        print('\nI knew you were an imposter!!')
        pause()

pause()
input('\n\nPress enter to exit!')
