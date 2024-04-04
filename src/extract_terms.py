import json
import settings
from preprocess_data import PreprocessData
import gemini
import prompts.extract_terms


class ExtractTerms:
    def __init__(self, data: str):
        self.data = data
        self.construct_prompt()

    def make_request(self, save=True):
        self.model = gemini.GeminiModel()
        self.model_response = self.model.get_response(self.prompt)[1:-1]

        if save:
            filename = __file__.rsplit('/', 1)[-1][:-3]
            saver = settings.SaveToCache(filename, self.model_response)
            saver.save()

    def construct_prompt(self):
        self.prompt = prompts.extract_terms.TERMS_EXTRACTION_PROMPT_TEMPLATE
        self.prompt = self.prompt.replace('{input}', f'"{self.data}"')

    def get_response(self) -> str:
        return self.model_response


def extracted_terms_to_list(gpt_response: str) -> list:
    json_data = json.loads(gpt_response)
    return json_data['entities']


if __name__ == '__main__':
    # data = PreprocessData(settings.RAW_ARTICLE_PATH)
    # data.parse()
    # data = data.string_for_prompt()
    # extract = ExtractTerms(data)
    # extract.make_request()
    # response = extract.get_response()
    # print(response)
    # with open('cache/extract_terms_1712065756.txt', 'r') as f:
    #     s = '\n'.join(f.readlines())
    #     print(extracted_terms_to_list(s)) # <- works!!!
    #     print(type(extracted_terms_to_list(s)[0][1][0])) # <- int!!!
    pass
