print("Welcome to the Rock-Paper-Scissors Computer Competition!")
print("Find out if you have what it takes to be a Champion!")
while True:
    play = input ("Do you want to continue?...(yes or no)...").lower()
    if play == "yes":
        competitor_selection = (input("Make your choice from the following selection: Rock, Paper, Scissors.......")).lower()
        print(competitor_selection)
        import random
        computer_selections =['Rock', 'Paper', 'Scissors']
        computer_selection = random.choice(computer_selections).lower()
        print(computer_selection)
        result = (competitor_selection+ " vs. " +computer_selection).lower()
        print(result)
        if result == 'rock vs. rock':
            print("It is a draw! Better luck next time! Please try again!")
        elif result == 'scissors vs. scissors':
            print("It is a draw! Better luck next time! Please try again!")
        elif result == 'paper vs. paper':
            print("It is a draw! Better luck next time! Please try again!")
        elif result == 'rock vs. scissors':
            print("Congratulations!!! You Won!! Please celebrate!! Go to Disney Land!!")
        elif result == 'scissors vs. paper':
            print("Congratulations!!! You Won!! Please celebrate!! Go to Disney Land!!")
        elif result == 'paper vs. rock':
            print("Congratulations!!! You Won!! Please celebrate!! Go to Disney Land!!")
        else:
            print ("Unfortunately you lost!! Hopefully you will do a better job making your choices next time!! The computer is tough so you must really think hard!!")
    else:
        print("Thank you for coming to our site! Please come again")
        break