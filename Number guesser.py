#game - Number guesser
import random
import time

def ChangeArr(ChancesArr, UserNum, gl):
    if gl == 0:
        if ChancesArr[0] == "":
            ChancesArr[0] = UserNum
            return ChancesArr
        elif UserNum > ChancesArr[0]:
            ChancesArr[0] = UserNum
            return ChancesArr
        else:
            return ChancesArr


    else:
        if ChancesArr[2] == "":
            ChancesArr[2] = UserNum
            return ChancesArr
        elif UserNum  < ChancesArr[2]:
            ChancesArr[2] = UserNum
            return ChancesArr
        else:
            return ChancesArr
    

def UIrender(ChancesArr):
    print("-------"*3)

    for i in range(3):
        space = round((5-len(str(ChancesArr[i]))) / 2) 
        print("|" + " "*space + f"{ChancesArr[i]}" + " "*(5-space-len(str(ChancesArr[i]))) + "|" , end="")

    print(end="\n")
    print("-------"*3)

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

        StartTime = time.time()
        ChancesArr = [""]*(chances+1)
        ChancesArr[1] = "?"
        print("Let's start the game!")
        for i in range(chances):
            nonerror = True
            print("\n" + f"it's {chances - i} attempts left" + "\n")
            UIrender(ChancesArr)
            while (nonerror):
                try:
                    UserNum = int(input("\nEnter your guess: "))
                    nonerror = False
                except ValueError:
                    print("Invalid number, Try again")
            if UserNum == number:
                print("\nCongratulations! You won\n")
                return attempts, time.time() - StartTime
            elif UserNum > number:
                print(f'No, my number is less than {UserNum}. Try again')
                attempts += 1
                ChancesArr = ChangeArr(ChancesArr, UserNum, 1)
                UIrender(ChancesArr)
            else:
                print(f'No, my number is greater than {UserNum}. Try again')
                attempts += 1
                ChancesArr = ChangeArr(ChancesArr, UserNum, 0)
                UIrender(ChancesArr)
        return 0, time.time() - StartTime

while True:
    result = Main()
    WoL = result[0]
    Alltime = result[1]
    if WoL == 0:
        print("\nYou lose, but it's just a game! Try again!")
        print(f"It took {Alltime} seconds\n")
    else:
        print(f"Good job you won with {WoL} attempts! Try again!")
        print(f"It took {Alltime} seconds\n")
