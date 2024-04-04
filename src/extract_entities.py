from preprocess_data import PreprocessData
from extract_terms import ExtractTerms
import gemini
import settings
import prompts.extract_entities
import json


class ExtractEntities:
    def __init__(self, data: str, terms: str):
        self.data = data
        self.terms = terms
        self.construct_prompt()

    def make_request(self, save=True):
        self.model = gemini.GeminiModel()
        self.model_response = self.model.get_response(self.prompt)[1:-1]

        if save:
            filename = __file__.rsplit('/', 1)[-1][:-3]
            saver = settings.SaveToCache(filename, self.model_response)
            saver.save()

    def construct_prompt(self):
        self.prompt = prompts.extract_entities.ENTITY_EXTRACTION_PROMPT_TEMPLATE
        self.prompt = self.prompt.replace('{input_data}', f'"{self.data}"')
        self.prompt = self.prompt.replace('{input_terms}', f'"{self.terms}"')

    def get_response(self) -> str:
        return self.model_response


def to_list_of_entities(json_str_entities: str, json_str_anaphors: str):
    entities = json.loads(json_str_entities)
    anaphors = json.loads(json_str_anaphors)

    names_and_indices = []
    anaphors_dict = {}

    for entity in entities['entities']:
        name, start_ind = entity
        start_ind = start_ind[0]
        names_and_indices.append([name, start_ind])

        if name not in anaphors_dict:
            anaphors_dict[name] = []

    for anaphor in anaphors['anaphors']:
        name = anaphor[0]
        anaphors_list = anaphor[1:]

        for anaphor_elem in anaphors_list:
            anaphor_text, ind = anaphor_elem
            names_and_indices.append([anaphor_text, ind])

            if name not in anaphors_dict:
                anaphors_dict[name] = []
            anaphors_dict[name].append(anaphor_text)

    return names_and_indices, anaphors_dict


if __name__ == '__main__':
    data = ''
    terms = ''
    with open('cache/extract_terms_1712065756.txt', 'r') as f:
        terms = '\n'.join(f.readlines())
    with open('data/raw_article.txt', 'r') as f:
        data = '\n'.join(f.readlines())
    ex = ExtractEntities(data, terms)
    ex.make_request()
    print(ex.get_response())
