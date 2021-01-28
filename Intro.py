import time

with open("location.txt", "a") as f:
    f.write("city\n")

print("Welcum to the city of Night")

#creating suspense
i = 1
while i < 4:
    print(".")
    time.sleep(1)
    i += 1

print("Great adventurer, what is your name?")
name = input(">>> ")

print("Great, it is an honor to welcome you,", name + ", to the city.\nI recomend you go to the caves to explore.")