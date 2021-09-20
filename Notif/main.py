from pynotifier import Notification
from random import randint

num = randint(0, 10)

lower = int(input("Enter Lower Number: "))
upper = int(input("Enter Upper Number: "))


if num >= lower and num <= upper:
    print("Yes, the number is in between", lower, "and", upper)
else:
    print("No, the number is in between", lower, "and", upper)


lower = int(input("Enter Lower Number: "))
upper = int(input("Enter Upper Number: "))


if num >= lower and num <= upper:
    print("Yes, the number is in between", lower, "and", upper)
else:
    print("No, the number is in between", lower, "and", upper)


guess = int(input("Guess the number: "))

if guess == num:
    notif_title = "You Won"
    notif_description = "Yes the number is " + str(num)
else:
    notif_title = "You Lost"
    notif_description = "The number is " + str(num)

Notification(
    title=notif_title,
    description=notif_description,
    duration=5,
    urgency="normal",
).send()
