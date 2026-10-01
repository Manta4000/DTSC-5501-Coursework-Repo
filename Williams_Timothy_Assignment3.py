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
    self = self.copy()
    for last in range(len(self)-1, 0, -1):
        for interior in range(last):
            if self[interior] > self[interior+1]:
                self[interior], self[interior+1] = self[interior+1], self[interior]
    return self


### Selection Sort

def selectionSort(self):
    self = self.copy()
    for exterior in range(len(self)-1):
        min_index = exterior
        for interior in range(exterior+1, len(self)):
            if self[interior] < self[min_index]:
                min_index = interior

        self[exterior], self[min_index] = self[min_index], self[exterior]
    return self


### Insertion Sort

def insertionSort(self):
    self = self.copy()
    for exterior in range(1, len(self)):
        temp = self[exterior]
        interior = exterior
        while interior > 0 and temp < self[interior-1]:
            self[interior] = self[interior-1]
            interior -= 1
        self[interior] = temp
    return self

### Merge Sort

def mergeSort(self, low, mid, high):
    self = self.copy()

    def sort_range(start, end):
        if end - start < 2:
            return
        middle = (start + end) // 2
        sort_range(start, middle)
        sort_range(middle, end)
        left_side = self[start:middle].copy()
        right_side = self[middle:end].copy()
        i = j = 0
        for k in range(start, end):
            if i == len(left_side):
                self[k] = right_side[j]
                j += 1
            elif j == len(right_side) or left_side[i] <= right_side[j]:
                self[k] = left_side[i]
                i += 1
            else:
                self[k] = right_side[j]
                j += 1

    sort_range(0, len(self))
    return self

### Quick Sort

def quicksort(
        self, low=0, high=None,
        key=None):
    self = self.copy()
    if high is None:
        high = len(self) - 1

    def sort_range(start, end):
        if start >= end:
            return
        pivot = self[(start + end) // 2]
        i, j = start, end
        while i <= j:
            while self[i] < pivot:
                i += 1
            while self[j] > pivot:
                j -= 1
            if i <= j:
                self[i], self[j] = self[j], self[i]
                i += 1
                j -= 1
        if start < j:
            sort_range(start, j)
        if i < end:
            sort_range(i, end)

    sort_range(low, high)
    return self

### BOGO Sort

def bogoSort(self):
    self = self.copy()
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(len(self) - 1):
            if self[i] > self[i + 1]:
                isSorted = False
                break
        if not isSorted:
            random.shuffle(self)
    return self

### Select only 10 elements from n for BOGO sort

n_bogo = n[:10]

### Part 2: Testing & Performance Comparison

begin_time = time.perf_counter()
BubbleSort(n)
end_time = time.perf_counter()
bubble_time = end_time - begin_time
print(f"Bubble Sort Time: {bubble_time}")

begin_time = time.perf_counter()
selectionSort(n)
end_time = time.perf_counter()
selection_time = end_time - begin_time
print(f"Selection Sort Time: {selection_time}")

begin_time = time.perf_counter()
insertionSort(n)
end_time = time.perf_counter()
insertion_time = end_time - begin_time
print(f"Insertion Sort Time: {insertion_time}")

begin_time = time.perf_counter()
mergeSort(n, 0, len(n)//2, len(n))
end_time = time.perf_counter()
merge_time = end_time - begin_time
print(f"Merge Sort Time: {merge_time}")

begin_time = time.perf_counter()
quicksort(n)
end_time = time.perf_counter()
quick_time = end_time - begin_time
print(f"Quick Sort Time: {quick_time}")

begin_time = time.perf_counter()
bogoSort(n_bogo)
end_time = time.perf_counter()
bogo_time = end_time - begin_time
print(f"Bogo Sort Time: {bogo_time}")

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.bar(['Bubble', 'Selection', 'Insertion', 'Merge', 'Quick'], [bubble_time, selection_time, insertion_time, merge_time, quick_time])
plt.xlabel('Sorting Algorithms')
plt.ylabel('Time (seconds)')
plt.title('Performance Comparison of Sorting Algorithms')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

""" Discussion Section 
The fastest sorting algorithm of our test was Quick Sort. 
The three fastest algorithms were Insertion, Merge, and Quick Sort from mid to absolute fastest.
While the slowest sorting algorithm of our test was Bubble sort and BOGO sort.

The listed times of the algorithms are as follows:
Bubble Sort Time: 0.1618159000063315
Selection Sort Time: 0.085069700027816
Insertion Sort Time: 0.07833280006889254
Merge Sort Time: 0.004793899948708713
Quick Sort Time: 0.0027033999795094132
Bogo Sort Time: 50.84128159994725

I am not exactly counting BOGO sort, even though it was fastest since it only used n=10 elements,
as opposed to the other algorithms which used the full dataset.

Performance Analysis
Algorithmic performance is dependent on the size and distribution of the input data.
Given Quick Sort's average-case time complexity of O(n log n), it performed well under typical scenarios.
While Insertion Sort showed strong performance in this test, it's time complexity of O(n^2) means it may not scale as well with 
increasingly large datasets.

Bubble sort most accurately reflects its O(n^2) time complexity in this test across the full dataset.
I also believe that the randomized selection of numbers in n contributed to space complecity which 
may have skewed performance to favor certain algorithms.
"""

"""
Generative AI review section
Model Used: Claude Sonnet 5

Prompt: 'Review my implementation of Merge, Quick, and Bubble Sort. Please refrain from replacing 
or correcting them immediately. Identify the accuracy/correctness, readability, and replicability 
of the code.'

Response Summary:

Bubble sort: Correct implementation, the nested loops with last and adjacent swaps reliably create a 
sorted copy. The readability is good but unconventional. The replicability is high due to the straightforward logic.

Merge sort: the logic is correct and it manages to sort properly, but the low, mid, and high parameters are apparently dead code.
Since the interior function sort_range always recurses over the entire array irregardless of what's passed in.
Because of this readability suffers.

Quick sort: The pivot selection is proper and has good recursive partitioning. Readability is good and consistent with the Merge sort
structure. Apparently aside from an unused key=None parameter 'that suggests unfinished custom-comparator support.'
"""

### AI Updated Bubble, Merge, and Quick Sort + performance

### AI Enhanced Bubble 

def bubbleSort2(arr):
    arr = arr.copy()
    for last in range(len(arr) - 1, 0, -1):
        for interior in range(last):
            if arr[interior] > arr[interior + 1]:
                arr[interior], arr[interior + 1] = arr[interior + 1], arr[interior]
    return arr

### AI Enhanced Merge 

def mergeSort2(arr, low=0, mid=None, high=None):
    arr = arr.copy()
    if high is None:
        high = len(arr)
    if mid is None:
        mid = (low + high) // 2

    def sort_range(start, end):
        if end - start < 2:
            return
        middle = (start + end) // 2
        sort_range(start, middle)
        sort_range(middle, end)
        left_side = arr[start:middle].copy()
        right_side = arr[middle:end].copy()
        i = j = 0
        for k in range(start, end):
            if i == len(left_side):
                arr[k] = right_side[j]
                j += 1
            elif j == len(right_side) or left_side[i] <= right_side[j]:
                arr[k] = left_side[i]
                i += 1
            else:
                arr[k] = right_side[j]
                j += 1

    sort_range(low, high)
    return arr

### AI Enhanced Quick Sort

def quicksort2(arr, low=0, high=None, key=None):
    arr = arr.copy()
    if high is None:
        high = len(arr) - 1
    if key is None:
        key = lambda x: x

    def sort_range(start, end):
        if start >= end:
            return
        pivot = key(arr[(start + end) // 2])
        i, j = start, end
        while i <= j:
            while key(arr[i]) < pivot:
                i += 1
            while key(arr[j]) > pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        if start < j:
            sort_range(start, j)
        if i < end:
            sort_range(i, end)

    sort_range(low, high)
    return arr

### Performance Test of AI Enhanced Sorts

##Bubble Sort 2
begin_time = time.perf_counter()
bubble_sorted = bubbleSort2(n)
end_time = time.perf_counter()
bubble_time = end_time - begin_time
print(f"Bubble Sort 2 Time: {bubble_time}")

##Merge Sort 2
begin_time = time.perf_counter()
merge_sorted = mergeSort2(n)
end_time = time.perf_counter()
merge_time = end_time - begin_time
print(f"Merge Sort 2 Time: {merge_time}")

##Quick Sort 2
begin_time = time.perf_counter()
quick_sorted = quicksort2(n)
end_time = time.perf_counter()
quick_time = end_time - begin_time
print(f"Quick Sort 2 Time: {quick_time}")


"""
Human v. AI Enhanced Sorts

Correctness: Both sorts were correct in their implementation and produced the expected sorted output.
Readability: The AI-enhanced versions of the sorting algorithms are more readable and maintainable 
compared to their human-written counterparts. Mostly because of small errors I made while implementing 
the first versions.
Efficiency: The AI-enhanced versions of the sorting algorithms are more efficient in terms of speed and resource usage compared 
to the original versions.

Algorithm Implementation: I'd argue that both the original and the AI enhanced are nearly identical in terms of their core logic and structure.
The only difference being finer details in readability and maintainability.

The improvements suggested by the AI include better variable names, more concise code, and improved error handling. All of which it
successfully did.

Times for AI-built algorithms:

Bubble Sort 2 Time: 0.2088454000186175
Merge Sort 2 Time: 0.006341799977235496
Quick Sort 2 Time: 0.0044992000330239534
"""

"""
Reflection Section

1) I think I was able to figure out the logic of the sorting algorithms on my own fairly well, and then
come up with implementations for each one.

2) I could use better understanding of OOP concepts, which I am still developing, but made an honest attempt
based on what I have learned from textbooks and online resources. I confused some things such as using dead code 
in my merge sort implementation, but that comes with learning territory.

3) The AI was very helpful in identifying areas for improvement and suggesting more efficient implementations.
Specifically, the AI helped me optimize the code structure and improve the overall performance of the sorting algorithms.

4) A couple of suggestions the AI got wrong were in the handling of edge cases, specifically in the quick sort implementation, by 
I think the AI overemphasized certain optimizations at the expense of others.

5) Hilariously, the AI's suggestions led to a slightly worse performing bubble, merge, and quick sort implementations in terms of speed.
I think this may have to do with the specific optimizations suggested by the AI, which might not be optimal for all cases or datasets. Mine was probably 
more generic in structure.

6) Conclusion
I learned that while AI can provide valuable insights and optimizations, it's important to critically evaluate its suggestions and consider 
the specific context and requirements of the problem at hand. The AI's suggestions, while often helpful, may not always be optimal for 
every situation or dataset. Additionally, the experience highlighted the importance of understanding the underlying algorithms and not 
relying solely on AI suggestions. Having implemented self-coded versions based on contextual understanding, I succeeded in creating implementations 
that were both correct and efficient, even if I sacrificed some optimization for generality because of my superficial understanding.
"""