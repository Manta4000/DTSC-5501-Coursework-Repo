#Chapter 2. Arrays from Data Structures & Algorithms in Python, 2nd Edition by Goodrich, Tamassia, Goldwasser

####9.8.2026
# Example uses OrderedArray class to encapsulate underlying list and provide methods for searching and inserting elements in sorted order. 
# The class maintains the sorted order of the array as elements are added or removed.

def find(self, item):
    lo = 0
    hi = self.__nItems - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if self.__a[mid] == item:
            return mid
        elif self.__a[mid] < item:
            lo = mid + 1
        else:
            hi = mid -1
    return lo

class OrderedArray(object):
    def __init__(self, initialSize):
        self.__a = [None] * initialSize
        self.__nItems = 0

    def get(self, n):
        if 0 <= n and n < self.__nItems:
            return self.__a[n]
        raise IndexError("Index" + str(n) + "is out of range")

    def travers(self, function=print):
        for j in range(self.__nItems):
            function(self.__a[j])

    def __str__(self):
        ans = "["
        for i in range(self.__nItems):
            if len(ans) > 1:
                ans += ", "
            ans += str(self.__a[i])
        ans += "]"
        return ans
    