#Creating a master mind gussing game 
#1-Generate a random code
#2-Make The user guess the code
#3-Compare the guess
#4-Tie the game together
import random
colors=["B","G","R","W","Y","O"]
TRIES=10
CODE_LENGTH= 4

# A function to generate the correct answer
def computer_Choice():
    code= []
    for i in range(CODE_LENGTH):
        color=random.choice(colors)
        code.append(color)
    return code

# A function to allow the user to guess
def guess_code():

    while True:
        userGuess= input("Guess: ").upper().split(" ")
        
        #check if the user entered the correct number of colors + if they exist
        if len(userGuess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors")
            continue

        for color in userGuess:
            if color in colors:
                break
            else:
                print(f"Invalid color: {color}. Try again")
                break    
        return userGuess

#A function to actually check and compare
def check_code(userGuess, real_code):
    color_counts ={}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color]=0
        color_counts[color]+= 1

    for userGuess_color, real_color in zip(userGuess, real_code):
        if userGuess_color == real_color:
            correct_pos+=1
            color_counts[userGuess_color]-=1

    for userGuess_color, real_color in zip(userGuess, real_code):
        if (userGuess_color in real_color )and color_counts[userGuess_color]>0:
            incorrect_pos+=1
            color_counts[userGuess_color]-=1
    return correct_pos, incorrect_pos

# Tie the game
def game():
    code = computer_Choice()
    for attempts in range(1, TRIES+1):
        user = guess_code()
        correct_pos, incorrect_pos = check_code(user, code)
        
        if correct_pos==CODE_LENGTH:
            print(f"You guessed the code in {attempts}tries!")
            break
        print(f"correct positions: {correct_pos}| Incorrect Positions: {incorrect_pos}")
    else: 
        print(f"You ran out of tries, the code was: {code}")

if __name__ == "__main__":
    game()
    











