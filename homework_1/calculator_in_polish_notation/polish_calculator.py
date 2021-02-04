OPERATOR_PERMITTED_VALUES = {'+', '-', '*', '/', 'add', 'sub', 'mul', 'div'}


def calculate(operator: str, operand_1: int or float, operand_2: int or float):
    if operator == '+' or operator == 'add':
        return operand_1 + operand_2
    elif operator == '-' or operator == 'sub':
        return operand_1 - operand_2
    elif operator == '*' or operator == 'mul':
        return operand_1 * operand_2
    elif operator == '/' or operator == 'div':
        return operand_1 / operand_2


def str_to_list(my_input):
    my_list = my_input.split()
    for index, item in enumerate(my_list):
        if item.isdecimal():
            my_list[index] = int(item)
        elif is_number(''.join(x for x in item if x != '.')) and '.' in item:
            my_list[index] = float(item)
    return my_list


def valid_input(input_list):
    result = True
    for item in input_list:
        if item not in OPERATOR_PERMITTED_VALUES and type(item) != int and type(item) != float:
            return False
    return result


def is_operator(list_element):
    return list_element in OPERATOR_PERMITTED_VALUES


def is_number(list_element):
    return list_element.isdecimal()


def expression_simplification(my_list):
    simple_list = my_list.copy()
    operator_flag = False
    number_flag = False
    for index, item in enumerate(simple_list):
        if is_operator(item):
            operator_flag = True
            number_flag = False
            my_operator = item
        else:
            if not number_flag:
                number_flag = True
                my_number = item
            else:
                if operator_flag:
                    simple_list[index - 1] = 'Need delete after every loop'
                    simple_list[index - 2] = 'Need delete after every loop'
                    simple_list[index] = calculate(my_operator, my_number, item)
                    number_flag = False
                    operator_flag = False
    while 'Need delete after every loop' in simple_list:
        simple_list.remove('Need delete after every loop')
    return simple_list


def recursive_simplification(new_list):
    if len(new_list) == 1:
        return new_list[0]
    return recursive_simplification(expression_simplification(new_list))


my_expression = input('Expression: ')
expression_list = str_to_list(my_expression)
print('Result: ', recursive_simplification(expression_list))