

numbers = [62, 66, 94, 97, 25, 11, 68, 54, 48, 67]

total = 0

for numbers in numbers:
    
    remainder = numbers % 2
    if remainder == 0:
        total = total + numbers
        print(total)

return total
        
