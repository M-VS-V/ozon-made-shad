import random
import numpy as np
commands  = ['insert', 'delete', 'exists', 'next', 'prev']
values = range(-10, 10)
n = 20
result = []

random.seed(5)
values = np.random.choice(range(0,5),n, replace=True)
indexies = np.random.choice(range(0,len(commands)),n,replace=True)

for v, i in zip(values, indexies):
    res = f'{commands[i]} {v}'
    result.append(res)

print("\n".join(result))