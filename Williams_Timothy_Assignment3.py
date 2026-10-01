"DTSC 5501 - 9.30.2026 - Assignment #3 - Timothy Williams"

### Generate dataset

import numpy as np
import random

n = []
def randset(rand):
    for i in range(1000):
        rand == random.randint(1,10000)
        n.append(rand)
    return n
    

randset(random)
print(len(n))

###Bubble Sort
### Based on the book "Data Structures & Algorithms in Python" -- Canning et. al

def BubbleSort(self):
    for last in range(self.__nItems-1, 0, -1):
        for inner in range(last):
            if self.__a[inner] > self.__a[inner+1]:
                self.swap(inner, inner+1)

