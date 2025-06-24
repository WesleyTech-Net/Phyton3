from time import sleep
print(10 * "=", "TABUADA", 10 * "=")
num = int(input("Qual tabuada deseja? "))
for i in range (0, 11):
    sleep(1)
    print(f"{num} x {i:2} = ", num * i)
sleep(1)
print("FIM")