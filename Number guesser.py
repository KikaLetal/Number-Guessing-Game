#game - Number guesser
def UIrender():
    pass


def Main():
    StartMessage = "Hi, it's a Number guesser game\n"\
          "Try to guess my number!\n"\
          "it's between 1 and 100\n\n"\
          "Please select difficulty level:\n"\
          "1 - Easy (10 chances)\n"\
          "2 - Medium (5 chances)\n"\
          "3 - Hard (3 chances)\n"\

    print(StartMessage)      
    while True:
        try:
            dificult: int = int(input("your choice: "))
            if dificult not in [1, 2, 3]:  
                print("\nInvalid choice, please enter 1, 2, or 3.\n")
                continue
        except ValueError:
            print("\nWrong difficult, please choice 1-3 \n")
            continue
        match(dificult):
            case 1:
                print("\nGreat, You choise Easy level! You have 10 chances")     
                break           
            case 2:
                print("\nGreat, You choise Medium level! You have 5 chances")  
                break
            case 3:
                print("\nGreat, You choise Hard level! You have only 3 chances") 
                break 


Main()