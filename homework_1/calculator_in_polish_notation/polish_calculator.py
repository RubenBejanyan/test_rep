OPERATOR_PERMITTED_VALUES = {'+', '-', '*', '/', 'add', 'sub', 'mul', 'div'}


def calculate(operator: str, operand_1: float, operand_2: float):
    if operator == '+' or operator == 'add':
        return operand_1 + operand_2
    elif operator == '-' or operator == 'sub':
        return operand_1 - operand_2
    elif operator == '*' or operator == 'mul':
        return operand_1 * operand_2
    elif operator == '/' or operator == 'div':
        return operand_1 / operand_2


def valid_input(my_input):
    if len(my_input) != 3:
        print('Invalid expression')
        return False
    elif my_input[0] not in OPERATOR_PERMITTED_VALUES:
        print('Invalid operator')
        return False
    elif type(my_input[1]) != int and type(my_input[1]) != float:
        print('Invalid first operand')
        return False
    if type(my_input[2]) != int and type(my_input[2]) != float:
        print('Invalid second operand')
        return False
    return True


def sting_to_number(string):
    if '.' in string:
        return float(string)
    else:
        return int(string)


while True:
    my_expression = input('Expression: ')
    expression_list = my_expression.split()
    expression_list[1] = sting_to_number(expression_list[1])
    expression_list[2] = sting_to_number(expression_list[2])
    if valid_input(expression_list):
        print(calculate(expression_list[0], expression_list[1], expression_list[2]))
