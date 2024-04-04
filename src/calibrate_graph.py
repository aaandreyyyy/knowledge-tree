import extract_terms
import extract_entities
import extract_relations
import graph


class Calibration:
    def __init__(self):
        self.terms = extract_terms.ExtractTerms()
        self.entities = extract_entities.ExtractEntities()
        self.relations = extract_relations.ExtractRelations()

        self.apply_extractions()

    def apply_extractions(self):
        self.terms.make_request()
        self.entities.make_request()
        self.relations.make_request() # 100% this structure will be changed, since entities require terms and relations require both of them

    def constuct_graph(self) -> graph.Graph:
        pass

