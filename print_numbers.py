import numpy as np
from matplotlib import pyplot as plt

print([0, 7, 34, 12])
print(np.random.randint(0, 10, 10))

plt.plot(np.random.randint(0, 10, 100), color = 'red')
plt.savefig("test.png")
plt.close()
