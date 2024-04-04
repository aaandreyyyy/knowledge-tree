import json
import util.special_token


class Expression(util.special_token.SpecialToken):
    def __init__(self, str_token: str):
        assert(str_token.startswith('EXPRESSION_'))

        super().__init__(str_token)
        with open('data/special_tokens.json', 'r') as f:
            json_ = json.load(f)
            self.expression_json = json_['Expressions'][self.str_token]

        self.dependencies = self.expression_json['Depends']
        self.name = self.expression_json['Name']
        self.description = self.expression_json['Description']
        self.tex = self.expression_json['Tex']

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_tex(self) -> str:
        return self.tex

    def get_dependencies(self) -> list:
        return self.dependencies


if __name__ == '__main__':
    expr = Expression('EXPRESSION_1')
    print(expr.to_string())
    print(expr.get_id())
    print(expr.get_name())
    print(expr.get_description())
    print(expr.get_tex())
    print(expr.get_dependencies())
