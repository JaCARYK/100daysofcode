print("welcome to Jacobs pizza")

total_bill = 0

size = input("what size pizza do you want? S, M, or L: ")
pepperoni = input("do you want pepperoni on your pizza> Y or N: ")
extra_cheese = input("do you want extra cheese Y or N: ")

if size == "S":
    total_bill += 15

elif size == "M":
    total_bill += 20

elif size == "L":
    total_bill += 25

else:
    print("not a valid option. please try again")
    exit()

if pepperoni == "Y":
    if size == "S":
        total_bill += 2
    else:
        total_bill += 3

if extra_cheese == "Y":
    total_bill += 1

print(f"your total is: ${total_bill}")
