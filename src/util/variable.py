import json
import util.special_token


class Variable(util.special_token.SpecialToken):
    def __init__(self, str_token: str):
        assert(str_token.startswith('VARIABLE_'))

        super().__init__(str_token)
        with open('data/special_tokens.json', 'r') as f:
            json_ = json.load(f)
            self.variable_json = json_['Variables'][self.str_token]

        self.name = self.variable_json['Name']
        self.description = self.variable_json['Description']

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_json(self) -> str:
        return self.variable_json


if __name__ == '__main__':
    var = Variable('VARIABLE_1')
    print(var.get_description())
    print(var.get_name())
    print(var.get_id())
    print(var.to_string())
    print(str(var.get_json()))
