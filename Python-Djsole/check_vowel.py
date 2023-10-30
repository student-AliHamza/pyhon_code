# a# alphabet = input("enter a letter to check the vowels or not")

# # if alphabet.lower() in ('a','e','i','o','u'):
# #     print("vowels alphabets")
# # else:
# #     print("not a  vowel alphabet") 
# # Get a character from the user (assuming it's a single letter)
# char = input("Enter a single letter: ")

# # Convert the character to lowercase to handle both uppercase and lowercase letters
# char = char.lower()

# # Check if the character is a vowel
# if char in 'aeiou':
#     print(f"{char} is a vowel.")
# else:
#     print(f"{char} is a consonant.")
letters = input("enter a alphabet")
  
vowels = ['a','e','i','o','u','A','E','I','O','U'] 

if letters in vowels:
    print("vowels")
else:
    print("not a vowels")