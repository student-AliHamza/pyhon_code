sum = 0
while(True):
    
    user_input = (input('enter the price'))
    if user_input != 'q':
        sum = sum + int(user_input)
        print(f"order total for: {sum}")

    else:
        print(f"your total bill is {sum} thankyou for shoping this us")
        break