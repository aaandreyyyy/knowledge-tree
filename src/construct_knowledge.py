from neo4j import GraphDatabase
import json
data = ''
with open('cache/extract_relations_1712240042.txt', 'r') as f:
    data = '\n'.join(f.readlines())
json_ = json.loads(data)
rel_list = json_["relations"]
for i in rel_list:
    print(i)



# ['average prediction error', 'exponential growth', 'prediction horizon']
# ['exponential growth', 'refects', 'lyapunov instability']
# ['lyapunov instability', 'inherent', 'chaotic system']
# ['lyapunov instability', 'leads', 'horizon of predictability']
# ['horizon of predictability', 'satisfes', 'constraint:  ε(t) ≤ εmax']
# ['exponential growth', 'triggers', 'exponential error growth']
# ['error growth', 'regardless', 'prediction method']
# ['horizon of predictability', 'upper boundary', 'prediction horizon']
# ['predictive clustering approach', 'provides', 'exponential growth of the average pre-diction error']
# ['motifs', 'enable', 'forecasting']
# ['motifs', 'form', 'prediction models']
