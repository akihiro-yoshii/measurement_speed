import timeit
import random

from collections import deque

loop = 10**5
data_size = 10**5
data_range = (1, 10**9)

# list
cmp_list = [random.randint(*data_range) for _ in range(data_size)]
ret_list = timeit.timeit(
    lambda: cmp_list.insert(0, random.randint(*data_range)),
    number=loop)

# deque
cmp_deque = deque([random.randint(*data_range) for _ in range(data_size)])
ret_deque = timeit.timeit(
    lambda: cmp_deque.appendleft(random.randint(*data_range)),
    number=loop)

print(" list: {:6.3f}sec".format(ret_list))
print("deque: {:6.3f}sec".format(ret_deque))
