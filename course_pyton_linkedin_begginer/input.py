#First ask for some text, and them prompt "Enter 1 to uppercase and 2 to lowercase: " and then either upper or lowercase it

user_text = input('Enter some text: ')

choice = int(input('Enter 1 to uppercase and 2 to lowercase: '))


if choice == 1:
    print(user_text.upper())
else:
    print(user_text.lower())