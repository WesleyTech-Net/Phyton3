#TIME CONVERSTION
num = int(input("Time in seconds: "))

hours = num // 3600 #calculate the hour
minute = (num % 3600) // 60 #calculate the minute
seconds = num % 60 #calculate the second

print(f"{hours}:{minute}:{seconds}")