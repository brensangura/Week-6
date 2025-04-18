high_income = False
good_credit = True

if high_income or good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")


high_income = False
good_credit = True

if high_income and good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")


high_income = False
good_credit = True
student = False

if not student:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

high_income = False
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

# age should be between 18 and 65
age = 22
if age >= 18 and age <= 65:
    print("Eligible for loan")
else:
    print("Not eligible for loan")


if 10 == 10:
    print("Condition is True")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("C")

for number in range(3):
    print("attempt", number + 1, (number + 1)*2)


successful = True
for number in range(3):
    print("attempt")
    if successful:
        print("successful")
        break

successful = False
for number in range(3):
    print("attempt")
    if successful:
        print("successful")
        break
    else:
        print("Attempted 3 times and failed")


# nested loops putting one loop inside of another loop
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

print(type(5))
print(type(range(5.0)))

# iterable
for x in "Python":
    print(x)

for x in [1, 2, 3]:
    print(x)


for item in shopping_cart:
    print(item)

# wild loop used to repaeat something until a condition is met
while True:
    print("Hello")
    break

number = 100
while number > 0:
    print(number)
    number //= - 1


command = ""
while command != "quit":
    command = input(">").lower()
    print("ECHO", command)


# infinite loop - A loop that never ends
command = ""
while True:
    command = input(">").lower()
    if command == "quit":
        break
    else:
        print("ECHO", command)
