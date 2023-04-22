import pandas as pd

df = pd.DataFrame({
    'n':[0,1,2,3,4,5,6,7,8,9], 
    'question': ['q1','q2', 'q3','q4', 'q5', 'q6', 'q7','q8', 'q9','q10' ], 
    'type': ['slider' ,'multiple', 'slider', 'selectbox', 'slider' ,'multiple', 'slider', 'selectbox', 'slider', 'slider'], 
    'data': [[0,5], ['o1','o2','o3'], [0,5], ['b1','b2','b3'], [0,5], ['o1','o2','o3'], [0,5], ['b1','b2','b3'], [0,5], [0,5] ]})

df.to_csv('questions.csv')