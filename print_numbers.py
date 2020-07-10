import numpy as np, pandas as pd
#from matplotlib import pyplot as plt

print([0, 7, 34, 12])
print(np.random.randint(0, 10, 10))

# plt.plot(np.random.randint(0, 10, 100), color = 'red')
# plt.savefig("test.png")
# plt.close()

import os
os.makedirs("output_file", exist_ok = True)

pd.DataFrame({"h": [0, 1, 5, 3], "value": [0.2, 0.1, 0.32, 0.11]}).to_csv('output_file/test.csv', index = False)
