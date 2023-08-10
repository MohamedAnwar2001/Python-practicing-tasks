from calc import *

history = []

while True:
    command = input("Enter the command (add/sub/mult/div):").lower()

    if command not in {"add", "sub", "mult", "div"}:
        print("Invalid operation. Please enter a valid command.")
    else:
        try:
            number1 = int(input("Enter the first number: "))
            number2 = int(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
        else:
            if command == "add":
                result = add(number1, number2)
            elif command == "sub":
                result = sub(number1, number2)
            elif command == "mult":
                result = mult(number1, number2)
            elif command == "div":
                result = div(number1, number2)

            print(result)

            while True:  # Inner loopfir handling user response if he enters anything other than yes or stop
                response = input("Wanna make another operation? Say 'yes' to continue, 'stop' to exit: ").lower()
                if response in {"yes", "stop"}:
                    break
                else:
                    print("Invalid response. Please enter 'yes' to continue or 'stop' to exit.")

            if response == "stop":
                print("Exiting")
                break

            history.append(f"{result} \n")


with open("history.txt", "a") as f:
    f.write("\n".join(history))

with open("history.txt", "r") as f:
    print(f.read())
