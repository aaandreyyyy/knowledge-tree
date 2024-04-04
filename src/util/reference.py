import json
import util.special_token


class Reference(util.special_token.SpecialToken):
    def __init__(self, str_token: str):
        assert(str_token.startswith('REFERENCE_'))

        super().__init__(str_token)
        with open('data/special_tokens.json', 'r') as f:
            json_ = json.load(f)
            self.description = json_['References'][self.str_token]

    def get_description(self) -> str:
        return self.description


if __name__ == '__main__':
    ref = Reference('REFERENCE_3')
    print(ref.get_description())
    print(ref.get_id())
    print(ref.to_string())
