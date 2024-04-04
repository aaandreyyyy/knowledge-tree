TERMS_EXTRACTION_PROMPT_TEMPLATE = '''### Task:
You will receive text from mathematical article. Analyze text for terms, ideas, entites and phrases which have information about topic.
Focus on identifying instances of terms, ideas, entites, concepts of article. You don't need to classify which word belongs to which class, just classify if word belong to at least one of them.
Provide the entities and their character position indicies within the text.

All entity types including their detailed definition are listed as follow.
### Definition:
"term/idea/concept": Some mathematical knowledge, which is being used to research topic of the article or is the topic of research.
"entity": Can be mathematical concept, but also can be any noun, which relates in some way with terms.


### Notice:
1. Text contains special tokens for: variables (VARIABLE), mathematical expressions (EXPRESSION), formulas (FORMULA) and references (REFERENCE).
Treat them as usual words. Formulas and expressions usually represent distinct entities.
2. Try extracting up to 5 terms and/or entities per paragraph (paragraph is about 5 consecutive sentences long).
3. Do not identify all pronouns as "anaphors". "anaphor" must relate to already found entity.
4. Length of entity can vary from one word to whole sentence.
5. If same term or its anaphor or synonim appears in text more than one time don't include it in output more than one time, just once.

### Examples:
Input:
"This paper introduces several novel strategies for multi-step-ahead prediction of chaotic time series.
Introducing a concept of “generalized z-vectors” (vectors of nonsuccessive time series observations) makes it possible to generate sets of possible prediction values for each point we are trying to predict.
Through examining these sets, unifed predictions are calculated, which are in turn used as a basis for predicting subsequent points.
The key diference between the strategy presented in this paper and its conventional counterparts is the concept of “nonpredictable” points (points which the algorithm categorized as “incalculable” and excluded from the calculations altogether)."
Explanation:
"This paper" is a entity, which refers to following research.
"multi-step-ahead prediction" is a term, which represents task which paper is trying to solve.
"chaotic time series" is a mathematical concept.
"“generalized z-vectors”" is a concept, which this article introduces.
"concept of “nonpredictable” points" is a concept, which this article introduces.
Output:
{{
    "entities": [
        ["This paper", [0, 9]],
        ["multi-step-ahead prediciton", [51, 77]],
        ["chaotic time series", [83, 100]],
        ["“generalized z-vectors”", [129, 150]],
        ["sets of possible prediction values", [234, 267]],
        ["concept of “nonpredictable” points", [547, 580]]
    ]
}}

### Input (Give passage):
{input}


### Output format:
## Entity respesentation:
- Each entity should be represented as ["entity name", [position_start, position_end]], where 'position_start' is the position of the first character of the entity name in the text, and 'position_end' is the position of the last character of the entity name in the entire text.
- Position is a number and starts from 0. You must calculate every position exactly.
- The extracted entity name must be the same as in the original text.

## Your output should be a single JSON object in the following format:
{{
    "entities": [
        ["entity name", [start, end]]
    ]
}}

## Output: '''
