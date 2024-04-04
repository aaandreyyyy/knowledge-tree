import json
import util.special_token
from util.equasion_type import EquasionType, get_equasion_type_from_string
from util.expression import Expression


class Formula(util.special_token.SpecialToken):
    def __init__(self, str_token):
        assert(str_token.startswith('FORMULA_'))

        super().__init__(str_token)
        with open('data/special_tokens.json', 'r') as f:
            json_ = json.load(f)
            self.formula_json = json_['Formulas'][self.str_token]

        self.equasion_type = get_equasion_type_from_string(self.formula_json['Equasion type'])
        self.left_expression = Expression(self.formula_json['Left expression'])
        self.right_expression = Expression(self.formula_json['Right expression'])
        self.description = self.formula_json['Description']

    def to_string(self, type=1) -> str:
        return FormulaRepresentation(self).to_string(type)

    def get_equasion_type(self) -> EquasionType:
        return self.equasion_type

    def get_left_expression(self) -> Expression:
        return self.left_expression

    def get_right_expression(self) -> Expression:
        return self.right_expression

    def get_description(self) -> str:
        return self.description


class FormulaRepresentation:
    def __init__(self, formula: Formula):
        self.formula = formula

    def to_string(self, type: int) -> str:
        if type == 1:
            return self.representation1()
        if type == 2:
            return self.representation2()
        if type == 3:
            return self.representation3()
        raise ValueError('Representation type should be 1, 2 or 3')

    def representation1(self) -> str:
        '''
        represents formula as its string token
        '''
        return self.formula.str_token

    def representation2(self) -> str:
        '''
        represents formula as:
        FORMULA_I -> LEFT_EXPRESSION.TOKEN EQUASION_TYPE RIGHT_EXPRESSION.TOKEN
        '''
        return self.formula.get_left_expression().to_string() + ' '\
            + self.formula.get_equasion_type().to_string() + ' '\
            + self.formula.get_right_expression().to_string()

    def representation3(self) -> str:
        '''
        represents formula as:
        FORMULA_I -> LEFT_EXPRESSION(VARIABLE_K1, VARIABLE_K2, ...) EQUASION_TYPE RIGHT_EXPRESSION(VARIABLE_T1, VARIABLE_T2, ...)
        '''
        return 'TODO'


if __name__ == '__main__':
    f = Formula('FORMULA_1')
    print(f.get_equasion_type().to_string())
    print(f.get_left_expression().to_string())
    print(f.get_right_expression().to_string())
    print(f.to_string())
    print(f.to_string(type=2))
    print(f.get_description())
