DTSC 5501 - 9.30.2026 - Assignment #3 - Timothy Williams"

### Generate dataset

import numpy as np
import random
import time 

n = np.array([])
def randset(rand):
    global n
    for _ in range(1000):
        rand = random.randint(1,10000)
        n = np.append(n, rand)
    return n
    

randset(random)
print(len(n))