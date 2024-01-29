import random
import time
# Implementation of binary search algorithm

# We will prove that it is faster than a naive search

#Naive search is just checking every item in the list one by one
#Binary Search finds a midpoint and then does a less than or greater than comparison. It then does this again on the next sub array.

# For naive search, if we find what we want, return the index, else return -1

def naive_search(mylist, target):
    #example of naive search
    for i in range(len(mylist)):
        if mylist[i] == target:
            return i 
    return -1
    
def binary_search(mylist, target, low = None, high = None):
    if low == None:
        low = 0
    if high == None:
        high = len(mylist) - 1
    if high < low:
        return -1
    midpoint = (low + high) // 2
    if mylist[midpoint] == target:
        return midpoint
    elif target < mylist[midpoint]:
        return binary_search(mylist, target, low, midpoint - 1)
    else:
        return binary_search(mylist, target, midpoint + 1, high)

if __name__ == '__main__':
    #l = [1,3,5,10,12]
    #t = 10
    #print(naive_search(l,t))
    #print(binary_search(l,t))
    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time:", (end - start)/length, "seconds.")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time:", (end - start)/length, "seconds.")
