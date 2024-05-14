import json
from sklearn.metrics import precision_score, recall_score, f1_score
from difflib import SequenceMatcher


def calculate_metrics(model_sequences, human_sequences):
    y_true = [1 if seq in human_sequences else 0 for seq in model_sequences]
    y_pred = [1] * len(model_sequences)
    precision = precision_score(y_true, y_pred, average='weighted')
    recall = recall_score(y_true, y_pred, average='weighted')
    f1 = f1_score(y_true, y_pred, average='weighted')
    exact_matches = sum(1 for a, b in zip(model_sequences, human_sequences) if a == b)
    exact_match_ratio = exact_matches / len(human_sequences)
    levenshtein_distance = 0
    for a, b in zip(model_sequences, human_sequences):
        sm = SequenceMatcher(None, a, b)
        levenshtein_distance += sm.quick_ratio()
    levenshtein_distance /= len(human_sequences)
    return {
        'precision': precision,
        'recall': recall,
        'f1': f1,
        'exact_match_ratio': exact_match_ratio,
        'levenshtein_distance': levenshtein_distance
    }


original_text = '''This paper introduces several novel strategies for multi-step-ahead
prediction of chaotic time series. Introducing a concept of
“generalized z-vectors” (vectors of nonsuccessive time series observations)
makes it possible to generate sets of possible prediction
values for each point we are trying to predict.
Through examining these sets, unifed predictions are calculated,
which are in turn used as a basis for predicting subsequent points.
The key difference between the strategy presented in this paper and its
conventional counterparts is the concept of “nonpredictable” points
(points which the algorithm categorized as “incalculable” and
excluded from the calculations altogether). The results obtained for
the benchmark and real-world time series indicate that while
typically the number of nonpredictable points tends to grow
exponentially with the number of steps ahead to be predicted, the
average error for predicted points remains small and nearly constant.
Thus, we redefine the problem of multi-step-ahead
prediction as a two-objective optimization problem: on one hand,
we aim to minimize the number of nonpredictable points and
the average error among the predictable ones. The resulting
strategy demonstrates accurate results for both benchmark and real-
world time series, with the number of predicted steps
exceeding that of any other published algorithm.'''

marked_terms = ['This paper', 'multi-step-ahead prediction', 'chaotic time series',
                '“generalized z-vectors”', 'unifed predictions', 'strategy presented in this paper',
                'concept of “nonpredictable” points', 'number of nonpredictable points',
                'average error for predicted points', 'two-objective optimization problem',
                'real-world time series', 'predicted steps', 'subsequent points',
                'average error among the predictable ones', 'steps ahead to be predicted',
                'vectors of nonsuccessive time series observations', 'average error for predicted points']

model_terms = []
terms_path = 'cache/result.txt'
with open(terms_path, 'r') as f:
    json_ = json.load(f)['entities']
    model_terms = [item[0] for item in json_]
model_terms = model_terms[:19]

metrics = calculate_metrics(model_terms, marked_terms)

for metric in metrics:
    print(f'{metric}: {metrics[metric]}')
