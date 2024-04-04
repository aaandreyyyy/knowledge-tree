class SpecialToken:
    '''Parent class for special tokens'''

    def __init__(self, str_token: str):
        '''str_token is token which is found in raw txt article'''
        self.str_token = str_token
        self.id = self.str_token.split('_')[1]

    def to_string(self) -> str:
        return self.str_token

    def get_id(self) -> str:
        return self.id
