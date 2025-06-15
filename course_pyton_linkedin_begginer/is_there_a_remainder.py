def has_remainder(number1, number2):

    number1 = int(input('First number: '))
    number2 = int(input('Second number: '))

    if number1 % number2 != 0:
        return True
    else:
        return False
