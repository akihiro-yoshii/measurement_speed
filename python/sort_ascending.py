import timeit
import random

import heapq

loop = 10
data_size = 10**5
data_range = (1, 10**9)

# list
def list_sort():
    cmp_list = [random.randint(*data_range) for _ in range(data_size)]
    cmp_list.sort()
    return cmp_list

ret_list = timeit.timeit(
    lambda: list_sort(),
    number=loop)

# heapify
def heapify_sort():
    cmp_list = heapq.heapify([random.randint(*data_range) for _ in range(data_size)])
    return cmp_list

ret_heapify = timeit.timeit(
    lambda: heapify_sort(),
    number=loop)

# heapq
def heapq_sort():
    cmp_list = []
    for _ in range(data_size):
        heapq.heappush(cmp_list, random.randint(*data_range))
    return cmp_list

ret_heapq = timeit.timeit(
    lambda: heapq_sort(),
    number=loop)


print("   list: {:6.3f}sec".format(ret_list))
print("heapify: {:6.3f}sec".format(ret_heapify))
print("  heapq: {:6.3f}sec".format(ret_heapq))
