import random
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"guessing a number between 1 and {x}:"))
        if guess < random_number:
            print("soory, guess again. too low")
        elif guess > random_number:
            print("soory guess again . too high")
    print(f"yay,congarts you have guessed the number{random_number}") 
  
def computer_guess(x):
    low = 1 
    high = x
    feedback = ''
    while feedback != 'C' and low != high:
        if low != high:
            guess = random.radiant(low,high)
        else:    
            guess = low
        guess = random.radient(low,high)
        feedback = input(f"Is {guess} too high (H), too low (L), or correct ( C)").lowercase
        if feedback == 'h':
            high = guess - 1
        if feedback == 'l':
            low = guess + 1
    print(f" yay computer guessed your number,{guess},correctly!")


guess(1000)