#001
def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2
    else:
        return "Undefined"

#002
def make_negative( number ):
    if number >= 0:
       return 0 - number
    else:
        return 0 + number

#003
def simple_multiplication(number) :
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9
