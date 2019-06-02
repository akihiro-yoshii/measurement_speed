import timeit
import random
from collections import deque

loop = 10**5
data_size = 10**5
data_range = (1, 10**9)

# list
cmp_list = [random.randint(*data_range) for _ in range(data_size)]
ret_list = timeit.timeit(
    lambda: cmp_list.insert(random.randint(0, len(cmp_list)), random.randint(*data_range)),
    number=loop)

# # deque
# # randint is not available on Python 3.4.3
# cmp_deque = deque([random.randint(*data_range) for _ in range(data_size)])
# ret_deque = timeit.timeit(
#     lambda: cmp_deque.insert(random.randint(0, len(cmp_deque)), random.randint(*data_range)),
#     number=loop)

print(" list: {:6.3f}sec".format(ret_list))
# print("deque: {:6.3f}sec".format(ret_deque))
