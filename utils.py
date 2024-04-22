import pandas as pd
data = pd.read_csv(data/titanic.csv)

def load_female_passengers():
    female_passengers = data[data['sex'] == 'female']
    return female_passengers
