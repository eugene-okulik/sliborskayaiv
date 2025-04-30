def operations(func):

    def wrapper():
        first, second = map(int, input("Enter two numbers separated by space: ").split())
        if first or second < 0:
            operator = '*'
        elif first > second:
            operator = '-'
        elif first < second:
            operator = '/'
        elif first == second:
            operator = '+'

        result = func(first, second, operator)
        print(f"{first} {operator} {second} = {result}")

    return wrapper


@operations
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


calc()
