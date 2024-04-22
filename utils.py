import pandas as pd
data = pd.read_csv(data/titanic.csv)

female_passengers = data[data['sex'] == 'female']
return female_passengers
