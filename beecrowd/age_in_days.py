
num = int(input("Insert your age in days: "))

year = num // 365
remaining_days = num % 365

month = remaining_days // 30
days = remaining_days % 30

print(f"{year} ano(s)")
print(f"{month} mes(es)")
print(f"{days} dia(s)")