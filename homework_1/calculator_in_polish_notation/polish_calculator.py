OPERATOR_PERMITTED_VALUES = {'+', '-', '*', '/', 'add', 'sub', 'mul', 'div'}


def calculate(operator: str, operand_1: int, operand_2: int):
    if operator == '+' or operator == 'add':
        return operand_1 + operand_2
    elif operator == '-' or operator == 'sub':
        return operand_1 - operand_2
    elif operator == '*' or operator == 'mul':
        return operand_1 * operand_2
    elif operator == '/' or operator == 'div':
        return operand_1 / operand_2


def valid_input(my_input):
    pass


def is_operator(list_element):
    return list_element in OPERATOR_PERMITTED_VALUES


def is_number(list_element):
    return list_element.isdecimal()


def expression_simplification(my_list):
    simpl_list = my_list.copy()
    operator_flag = False
    number_flag = False
    for i, item in enumerate(simpl_list):
        print(i, end=' ')
        if item in OPERATOR_PERMITTED_VALUES:
            operator_flag = True
            number_flag = False
            my_operator = item
        else:
            if not number_flag:
                number_flag = True
                my_number = int(item)
            else:
                if operator_flag:
                    simpl_list.pop(i-2)
                    simpl_list.pop(i-2)
                    simpl_list.pop(i-2)
                    simpl_list.insert(i-2, calculate(my_operator, my_number, int(item)))
                    number_flag = False
                    operator_flag = False
    return simpl_list


def recursive_simplification(new_list):
    print(new_list)
    if len(new_list) == 1:
        return new_list[0]
    return recursive_simplification(expression_simplification(new_list))


my_expression = input('Expression: ')
expression_list = my_expression.split()
#print(recursive_simplification(expression_list))
a = expression_simplification(expression_list)
print(expression_list, len(expression_list))
print(a, len(a))
print(expression_simplification(a), len(expression_simplification(a)))
