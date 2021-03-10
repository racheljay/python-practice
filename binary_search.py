# Implementation of binary search algorithm

# Proving that binary search is faster than naive search

# naive search - scans entire list and asks if it is equal to the target
# if yes, return the index
# if no, then return -1

def naive_search(l, target):
    # example l = [1, 2, 6, 9]
    for i in l:
        print(i)
        if l[i] == target:
            return i
        else:
            return -1


# binary search will divide and conquer
# we will leverage the fact that our list is SORTED

# def binary_search(l, target, low=None, high=None):
#     if low is None:
#         low = 0
#     if high is None:
#         high = len(l) - 1

#     # what happens if it is not in the list
#     if high < low:
#         return -1
#     # example l = [1,3,5,10,12] should return 3
#     # 2 -- // means how many times will this go into length
#     midpoint = (low + high) // 2

#     if l[midpoint] == target:
#         return midpoint
#     elif target < l[midpoint]:
#         return binary_search(l, target, low, midpoint-1)
#     else:
#         #target > l[midpoint]
#         return binary_search(l, target, midpoint+1, high)


# if __name__ == '__main___':
l = [1, 3, 5, 10, 12]
target = 1
print(naive_search(l, target))
# print(binary_search(l, target))
