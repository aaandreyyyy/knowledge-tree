ENTITY_EXTRACTION_PROMPT_TEMPLATE = '''### Task:
You will receive text from mathematical article. Also you will receive list of terms.
Analize text for synonims and/or anaphors. For each terms extract all its anaphors/synonims (if there are some).
Provide the terms' with indicies of their synonims/anaphors characters within the text.

### Definition:
"synonim": other word which mean same thing as given word. (e. g. "this article introduces concept of z-vectors. ... In this paper problem of predcting points solved..." "paper" and "article" are synonims)
"anaphor": is the word which referes and means same thing as the word which it refers to (e. g. "this article introduces concept of z-vectors, they are important for predicting..." "z-vectors" and "they" are anaphors)


### Notice:
1. Text contains special tokens for: variables (VARIABLE), mathematical expressions (EXPRESSION), formulas (FORMULA) and references (REFERENCE).
Treat them as usual words.
2. Length of synonim/anaphort can vary from one word to whole sentence. Also number of found anaphors can vary, and can be zero in some cases.
3. Try extracting all pronous as anaphors (only which refer to given entities).

### Examples:
Input:
"This paper introduces several novel strategies for multi-step-ahead prediction of chaotic time series.
Introducing a concept of “generalized z-vectors” (vectors of nonsuccessive time series observations) makes it possible to generate sets of possible prediction values for each point we are trying to predict.
Through examining these sets, unifed predictions are calculated, which are in turn used as a basis for predicting subsequent points.
The key difference between the strategy presented in this paper and its conventional counterparts is the concept of “nonpredictable” points (points which the algorithm categorized as “incalculable” and excluded from the calculations altogether)."
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
Output:
{{
    "anaphors": [
        ["“generalized z-vectors”", ["(vectors of nonsuccessive time series observations)", 152]],
        ["sets of possible prediction values", ["these sets" , 328]]
    ]
}}


### Input (Give passage):
{input_data}
{input_terms}


### Output format:
- For each entity result should be represented as ["entity name", ["anaphor1 name", position_start]]. Where 'position_start' is the position of the first character of the anaphor name in the text.
- Position is a number and first charachter position is 0. You must calculate every position exactly.
- The extracted ana[hor] name must be the same as in the original text.

### Your output should be a single JSON object in the following format:
{{
    "anaphors": [
        ["entity name", ["anaphor/synonim name", start], ...]
    ]
}}

## Output: '''
