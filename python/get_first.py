import timeit
import random

from collections import deque

loop = 10**6
data_size = 10**5
data_range = (1, 10**9)

index = 0

# list
cmp_list = [random.randint(*data_range) for _ in range(data_size)]
ret_list = timeit.timeit(
    lambda: cmp_list[index],
    number=loop)

# deque
cmp_deque = deque([random.randint(*data_range) for _ in range(data_size)])
ret_deque = timeit.timeit(
    lambda: cmp_deque[index],
    number=loop)

# dict
cmp_dict = {}
for i in range(data_size):
    cmp_dict["{}".format(i)] = random.randint(*data_range)

index_str = "{}".format(index)
ret_dict = timeit.timeit(
    lambda: cmp_dict[index_str],
    number=loop)

print(" list: {:6.3f}sec".format(ret_list))
print("deque: {:6.3f}sec".format(ret_deque))
print(" dict: {:6.3f}sec".format(ret_dict))
