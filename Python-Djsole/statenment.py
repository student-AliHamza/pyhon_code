percentage = input("enter the percentage")
# typecasting ( from str to int )
percentage_int = float(percentage)
if percentage_int >= 100 or percentage_int < 0:
    print('invalid percentage')
elif percentage_int >= 90:
    print("your grade is A")
elif percentage_int >= 80 :
    print("your grade is B")
elif percentage_int >= 60 : 
    print("your grade is C")
elif percentage_int >= 45:
    print("your grade is D")
else:
    print("your grade is F")
 
