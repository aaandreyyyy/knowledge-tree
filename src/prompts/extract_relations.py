RELATIONS_EXTRACTION_PROMPT_TEMPLATE = '''### Task:
You will receive text from mathematical literature and list of named entities.
Analyze text for relations between these entities and extract them.

### Definition:
"entity": phrase which refers to terms/definitions/knowledges from article.
"relation": word or phrase which reflects how entities refer or interact with each other.


### Notice:
1. Text contains special tokens for: variables (VARIABLE), mathematical expressions (EXPRESSION), formulas (FORMULA) and references (REFERENCE).
Treat them as usual words.
2. Length of relation can vary from one word to sentence.
3. Try extracting all relations.

### Example:
Input:
"This paper introduces several novel strategies for multi-step-ahead prediction of chaotic time series.
Introducing a concept of “generalized z-vectors” (vectors of nonsuccessive time series observations) makes it possible to generate sets of possible prediction values for each point we are trying to predict.
Through examining these sets, unifed predictions are calculated, which are in turn used as a basis for predicting subsequent points.
The key difference between the strategy presented in this paper and its conventional counterparts is the concept of “nonpredictable” points (points which the algorithm categorized as “incalculable” and excluded from the calculations altogether)."
{{
    "entities": [
        ["This paper", 0]
        ["chaotic time series", 83],
        ["“generalized z-vectors”", 129],
        ["sets of possible prediction values", 234],
        ["concept of “nonpredictable” points", 547]
    ]
}}
Output:
{{
    "relations": [
        ["This paper", "introduces", "chaotic time series"],
        ["“generalized z-vectors”", "makes it possible to generate", "sets of possible prediction values"]
    ]
}}

# Input (Give passage):
{input}
{input_entity}

### Output format:
- For each found relation result should be represented as ["first_entity_name", "relation", "second_entity_name"]. Where 'first_entity_name' is name of first of two entities between which you have found relation, 'second_entity_name' is the name of the second of these entities. 'relation' is the name of found relation.
- The extracted relations and names must be the same as in the original text.

### Your output should be a single JSON object in the following format:
{{
    "relations": [
        ["first_entity_name", "relation", "second_entity_name"]
    ]
}}

## Output: '''


