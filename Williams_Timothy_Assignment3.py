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
        for interior in range(last):
            if self.__a[interior] > self.__a[interior+1]:
                self.swap(interior, interior+1)


### Selection Sort

def selectionSort(self):
    for exterior in range(self.__nItems-1):
        min = exterior
        for interior in range(exterior+1, self.__nItems):
            if self.__a[interior] < self.__a[min]:
                min = interior

        self.swap(exterior, min)


### Insertion Sort

def insertionSort(self):
    for exterior in range(1, self.__nItems):
        temp = self.__a[exterior]
        interior = exterior
        while interior > 0 and temp < self.__a[interior-1]:
            self.__a[interior] = self.__a[interior-1]
            interior -= 1
        self.__a[interior] = temp

### Merge Sort

def merg(self, low, mid, high):
    n = 0
    idxLow = low
    idxHigh = high

    while (idxLow < mid and 
           idxHigh < high):
        itemlo = self.__arr.get(idxLow)
        itemHi = self.__arr.get(idxHigh)
        if (self.__key(itemlo) <= self.__key(itemHi)):
            self.__work.set(n, itemlo)
            idxLow += 1
        else:
            self.__work.set(n, itemHi)
            idxHigh += 1
        n += 1

    while idxLow < mid:
        self.__work.set(
            n, self.__arr.get(idxLow))
        idxLow += 1
        n += 1

    while n > 0:
        n -= 1
        self.__arr.set(
            low + n, self.work.get(n))

### Quick Sort

def quicksort(
        self, low=0, high=None,
        key=None):
    if key is None:
        key = lambda value: value
    if high is None:
        high = len(self) - 1
    if low >= high:
        return

    pivot = self.choosePivot(low, high, key)

    highpart = self.partition(
        key(pivot),
        low, high, key)

    self.quicksort(low, highpart -1, key)
    self.quicksort(highpart, high, key)

### BOGO Sort

def bogoSort(self):
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(len(self.__a) - 1):
            if self.__a[i] > self.__a[i + 1]:
                isSorted = False
                break
    if not isSorted:
        random.shuffle(self.__a)

