
import pandas as pd
import random
 
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data)

data['human'] = 0
data['robot'] = 0

for i in range(len(data)):
    if data.loc[i, 'whoAmI'] == 'human':
        data.loc[i, 'human'] = 1
    else:
        data.loc[i, 'robot'] = 1

data.drop('whoAmI', axis=1, inplace=True)

print(data)

