from preprocess_data import PreprocessData
import extract_entities
import settings
import gemini
import prompts.extract_relations
import json


class ExtractRelations:
    def __init__(self, data_entities: str, article: str):
        self.article = article
        self.data = data_entities
        self.construct_prompt()

    def make_request(self, save=True):
        self.model = gemini.GeminiModel()
        self.model_response = self.model.get_response(self.prompt)

        if save:
            filename = __file__.rsplit('/', 1)[-1][:-3]
            saver = settings.SaveToCache(filename, self.model_response)
            saver.save()

    def construct_prompt(self):
        self.prompt = prompts.extract_relations.RELATIONS_EXTRACTION_PROMPT_TEMPLATE
        self.prompt = self.prompt.replace('{input}', f'"{self.article}"')
        self.prompt = self.prompt.replace('{input_entity}', f'"{self.data}"')

    def get_response(self) -> str:
        return self.model_response


def convert_list_to_json_string(result_list) -> str:
    entities = [item for item in result_list if isinstance(item, list) and len(item) == 2]
    entities_dict = {'entities': entities}
    entities_json = json.dumps(entities_dict)
    return entities_json


if __name__ == '__main__':
    terms = ''
    entities = ''
    with open('cache/extract_terms_1712065756.txt', 'r') as f:
        terms = '\n'.join(f.readlines())
    with open('cache/extract_entities_1712227713.txt', 'r') as f:
        entities = '\n'.join(f.readlines())
    article = ''
    with open('data/raw_article.txt', 'r') as f:
        article = '\n'.join(f.readlines())


    names, anaphors = extract_entities.to_list_of_entities(terms, entities)
    names = sorted(names, key=lambda x: x[1])
    data = convert_list_to_json_string(names)


    ex = ExtractRelations(data, article)
    ex.make_request()
    print(ex.get_response())
    #print(ex.prompt)
