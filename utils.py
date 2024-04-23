import pandas as pd
data = pd.read_csv('data/titanic.csv')

def load_male_passengers():
    male_passengers = data[data['sex'] == 'male']
    return male_passengers
print(load_male_passengers().head(10))