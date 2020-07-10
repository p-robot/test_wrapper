import numpy as np, pandas as pd
#from matplotlib import pyplot as plt

print([0, 7, 34, 12])
print(np.random.randint(0, 10, 10))

# plt.plot(np.random.randint(0, 10, 100), color = 'red')
# plt.savefig("test.png")
# plt.close()
pd.DataFrame({"h": [0, 1, 5, 3], "value": [0.2, 0.1, 0.32, 0.11]}).to_csv('test.csv', index = False)
