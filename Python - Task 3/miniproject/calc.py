def add(number1, number2):
    result = f"{number1}+{number2} = {number1 + number2}"
    return result


def sub(number1, number2):
    result = f"{number1}-{number2} = {number1 - number2}"
    return result


def mult(number1, number2):
    result = f"{number1}*{number2} = {number1 * number2}"
    return result


def div(number1, number2):
    try:
        result = f"{number1}/{number2} = {number1 / number2}"
    except ZeroDivisionError:
        result = "Error: Cannot divide by zero!"
    return result
