"DTSC 5501 - 9.30.2026 - Assignment #3 - Timothy Williams"

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

###Bubble Sort
### Based on the book "Data Structures & Algorithms in Python" -- Canning et. al

def BubbleSort(self):
    for last in range(len(self)-1, 0, -1):
        for interior in range(last):
            if self[interior] > self[interior+1]:
                self[interior], self[interior+1] = self[interior+1], self[interior]


### Selection Sort

def selectionSort(self):
    for exterior in range(len(self)-1):
        min_index = exterior
        for interior in range(exterior+1, len(self)):
            if self[interior] < self[min_index]:
                min_index = interior

        self[exterior], self[min_index] = self[min_index], self[exterior]


### Insertion Sort

def insertionSort(self):
    for exterior in range(1, len(self)):
        temp = self[exterior]
        interior = exterior
        while interior > 0 and temp < self[interior-1]:
            self[interior] = self[interior-1]
            interior -= 1
        self[interior] = temp

### Merge Sort

def mergeSort(self, low, mid, high):
    if mid <= low or high <= mid:
        return
    left_side = self[low:mid].copy()
    right_side = self[mid:high].copy()
    i = j = 0
    for k in range(low, high):
        if i == len(left_side):
            self[k] = right_side[j]
            j += 1
        elif j == len(right_side) or left_side[i] <= right_side[j]:
            self[k] = left_side[i]
            i += 1
        else:
            self[k] = right_side[j]
            j += 1

### Quick Sort

def quicksort(
        self, low=0, high=None,
        key=None):
    if high is None:
        high = len(self) - 1
    if low >= high:
        return self
    pivot = self[(low + high) // 2]
    i, j = low, high
    while i <= j:
        while self[i] < pivot:
            i += 1
        while self[j] > pivot:
            j -= 1
        if i <= j:
            self[i], self[j] = self[j], self[i]
            i += 1
            j -= 1
    if low < j:
        quicksort(self, low, j)
    if i < high:
        quicksort(self, i, high)
    return self

### BOGO Sort

def bogoSort(self):
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(len(self) - 1):
            if self[i] > self[i + 1]:
                isSorted = False
                break
        if not isSorted:
            random.shuffle(self)

### Select only 10 elements from n for BOGO sort

n_bogo = n[:10]

### Part 2: Testing & Performance Comparison

begin_time = time.perf_counter()
BubbleSort(n)

end_time = time.perf_counter()
print(f"Bubble Sort Time: {end_time - begin_time}")

begin_time = time.perf_counter()
selectionSort(n)
end_time = time.perf_counter()
print(f"Selection Sort Time: {end_time - begin_time}")

begin_time = time.perf_counter()
insertionSort(n)
end_time = time.perf_counter()
print(f"Insertion Sort Time: {end_time - begin_time}")

begin_time = time.perf_counter()
mergeSort(n, 0, len(n)//2, len(n))
end_time = time.perf_counter()
print(f"Merge Sort Time: {end_time - begin_time}")

begin_time = time.perf_counter()
quicksort(n)
end_time = time.perf_counter()
print(f"Quick Sort Time: {end_time - begin_time}")

begin_time = time.perf_counter()
bogoSort(n_bogo)
end_time = time.perf_counter()
print(f"Bogo Sort Time: {end_time - begin_time}")


""" Discussion Section 
The fastest sorting algorithm of our test was Insertion Sort. 
The three fastest algorithms were Insertion, Merge, and Quick Sort.
While the slowest sorting algorithm of our test was Selection and Bubble sort.
I am not exactly counting BOGO sort, even though it was fastest since it only used n=10 elements,
as opposed to the other algorithms which used the full dataset.

Performance Analysis
Algorithmic performance is dependent on the size and distribution of the input data.
Given Quick Sort's average-case time complexity of O(n log n), it performed well under typical scenarios.
This suggests that the pivot selection strategy in Quick Sort contributed to its under-performance in this particular case.
While Insertion Sort showed strong performance in this test, it's time complexity of O(n^2) means it may not scale as well with 
increasingly large datasets.

Bubble sort most accurately reflects its O(n^2) time complexity in this test across the full dataset.
I also believe that the randomized selection of numbers in n contributed to space complecity which 
may have skewed performance to favor certain algorithms.

"""

"""
Generative AI review section


"""