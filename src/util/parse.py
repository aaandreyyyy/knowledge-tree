from util.formula import Formula
from util.variable import Variable
from util.reference import Reference
from util.expression import Expression


def is_variable(token: str) -> bool:
    return token.startswith('VARIABLE_')


def is_formula(token: str) -> bool:
    return token.startswith('FORMULA_')


def is_reference(token: str) -> bool:
    return token.startswith('REFERENCE_')


def is_expression(token: str) -> bool:
    return token.startswith('EXPRESSION_')


def is_special_token(token: str) -> bool:
    return is_formula(token) or is_variable(token)\
        or is_expression(token) or is_reference(token)


def process_special_token(token: str):
    if not is_special_token(token):
        return None
    if is_variable(token):
        return Variable(token)
    if is_formula(token):
        return Formula(token)
    if is_reference(token):
        return Reference(token)
    if is_expression(token):
        return Expression(token)


if __name__ == '__main__':
    token = 'FORMULA_1'
    print(process_special_token(token).to_string(type=2))
