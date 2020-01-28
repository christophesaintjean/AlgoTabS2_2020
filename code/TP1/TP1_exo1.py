#import tqdm
from tqdm import tqdm, tqdm_gui
import matplotlib.pyplot as plt

L = [2, 3, 5, 19, -2] * 10
L2 = [x // 2 + 4 for x in L]

"""
for i in tqdm(L):
    pass
"""

plt.plot(L)
plt.plot(L2) 
plt.show()
