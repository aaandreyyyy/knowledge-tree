import settings
from util.parse import process_special_token
from util.formula import Formula


class PreprocessData:
    def __init__(self, path: str):
        with open(path, 'r') as f:
            self.raw_data = ' '.join(f.readlines())

    def parse(self):
        self.replaces()
        self.raw_data_list = self.raw_data.split(' ')

        self.parse_token_list()


    def replaces(self):
        self.raw_data = self.raw_data\
            .replace('\n', ' ')\
            .replace('.', ' .')\
            .replace(',', ' ,')

    def parse_token_list(self):
        self.parsed_token_list = []
        self.parsed_token_list_with_specials = []
        self.token_indexes = {}

        i = 0
        while i < len(self.raw_data_list):
            cur_token = self.raw_data_list[i].strip()

            if cur_token == '':
                i += 1
                continue

            processed = process_special_token(cur_token)
            if processed is not None:
                self.parsed_token_list_with_specials.append(processed)
            else:
                self.parsed_token_list_with_specials.append(cur_token)

            self.parsed_token_list.append(cur_token)
            if cur_token in self.token_indexes:
                self.token_indexes[cur_token].append(i)
            else:
                self.token_indexes[cur_token] = [i]

            i += 1

    def get_token_list(self) -> list:
        return self.parsed_token_list

    def get_token_list_with_specials(self):
        return self.parsed_token_list_with_specials

    def get_token_indexes(self) -> dict:
        return self.token_indexes

    def get_token_str_list(self, type=1) -> list:
        res = []
        for token in self.parsed_token_list_with_specials:
            if isinstance(token, str):
                res.append(token)
            elif isinstance(token, Formula):
                res.append(token.to_string(type=type))
            else:
                res.append(token.to_string())
        return res

    def string_for_prompt(self) -> str:
        return ' '.join(self.get_token_str_list(type=2))


def token_list_with_formulas_types(token_list_with_specials, type=1):
    res = []
    for token in token_list_with_specials:
        if isinstance(token, str):
            res.append(token)
        elif isinstance(token, Formula):
            res.append(token.to_string(type=type))
        else:
            res.append(token.to_string())
    return res


if __name__ == '__main__':
    data = PreprocessData(settings.RAW_ARTICLE_PATH)
    data.parse()
    #print(data.get_token_list())
    print('\n'.join(token_list_with_formulas_types(data.get_token_list_with_specials(), type=2)[:500]))
