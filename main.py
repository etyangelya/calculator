# a simmple python program that does a math operation based on user inputs
while (True):
    message = "hello welcoming to learning python with elya"
    print(message)
    number1 = int(input("enter a number:"))
    number2 = int(input("enter a second number:"))
    operation = input("what operation would you like to do + or -..?\t")
    if operation == "+":
        answer = number1 + number2
        print("answer=" + str(answer))
    elif operation == "-":
        answer = number1 - number2
        print("answer=" + str(answer))
    else:
        print("invalid")
    question = input("would you like to continue?\t")
    if question == "yes":
        continue
    elif question == "no":
        break
    else:
        print("invalid")
    continue

