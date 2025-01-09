#game - Number guesser
import random
def UIrender():
    pass

print("Hi, it's a Number guesser game\n"\
          "Try to guess my number!\n"\
          "it's between 1 and 100\n\n")
def Main():
    StartMessage = "Please select difficulty level:\n"\
          "1 - Easy (10 chances)\n"\
          "2 - Medium (5 chances)\n"\
          "3 - Hard (3 chances)\n"\

    print(StartMessage)      
    while True:
        attempts: int = 1 
        number: int = random.randint(1,100)
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
                chances: int = 10    
                       
            case 2:
                print("\nGreat, You choise Medium level! You have 5 chances")  
                chances: int = 5  
            
            case 3:
                print("\nGreat, You choise Hard level! You have only 3 chances") 
                chances: int = 3 

        print("Let's start the game!")
        for i in range(chances):
            UserNum = int(input("\nEnter your guess: "))
            if UserNum == number:
                print("\nCongratulations! You won\n")
                return attempts
            elif UserNum > number:
                print(f'No, my number is less than {UserNum}. Try again')
            else:
                print(f'No, my number is greater than {UserNum}. Try again')
        return 0

while True:
    result = Main()
    if result == 0:
        print("\nYou lose, but it's just a game! Try again!\n")
    else:
        print(f"Good job you won with {result} attempts! Try again!" + "\n")