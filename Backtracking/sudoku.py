def get_factorial(number: int):
    if (number == 1 or number == 0):
        return 1
    return number * get_factorial(number - 1)

factorial = get_factorial(20) * 0.413
print(factorial)