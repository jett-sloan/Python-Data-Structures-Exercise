from math import floor
def calculate(operation, a, b, make_int=False, message='The result is'):

    result = None

    if operation == 'add':
        result = a + b
    elif operation == 'subtract':
        result = a - b
    elif operation == 'multiply':
        result = a * b
    elif operation == 'divide':
        if b != 0:
            result = a / b
        else:
            return "Cannot divide by zero."
    else:
        return None  

    if make_int:
        result = int(result)

    return f'{message} {result}'

# Examples
print(calculate('add', 2.5, 4))
print(calculate('subtract', 4, 1.5, make_int=True))
print(calculate('multiply', 1.5, 2))
print(calculate('divide', 10, 4, message='I got'))
print(calculate('foo', 2, 3))



