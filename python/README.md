# 概要
Python3にてlist系データの各操作についての処理時間を計測する

# 目的
競技プログラミングでコンテスト中に毎回データ構造を考えており，
時間がもったいないので外部記憶化しておく．
必要な操作から適切なlistを選択できる情報をまとめる．
適宜増やしていく予定

# 前提条件
Python: 3.4.3

## データ挿入
### 先頭へのデータ挿入
`list`と`collections.deque`を比較
10万のデータに対して10万回データを追加して比較

[実装](/insert_first.py)
先頭への追加ではdequeを使う方が良い．

```text:result
 list: 12.834sec
deque:  0.226sec
```

### 末尾へのデータ挿入
`list`と`collections.deque`を比較
10万のデータに対して10万回データを追加して比較

<details><summary>実装</summary><div>

```python:insert_last.py
import timeit
import random
from collections import deque

loop = 10**5
data_size = 10**5
data_range = (1, 10**9)

# list
cmp_list = [random.randint(*data_range) for _ in range(data_size)]
ret_list = timeit.timeit(
    lambda: cmp_list.append(random.randint(*data_range)),
    number=loop)

# deque
cmp_deque = deque([random.randint(*data_range) for _ in range(data_size)])
ret_deque = timeit.timeit(
    lambda: cmp_deque.append(random.randint(*data_range)),
    number=loop)

print(" list: {:6.3f}sec".format(ret_list))
print("deque: {:6.3f}sec".format(ret_deque))
```
</div></details>
末尾への追加ならlist/dequeどちらでも良い

```text:result
 list:  0.236sec
deque:  0.235sec
```

## listのソート
### 昇順ソート
以下の3種を比較

- `list`を作成してから`list.sort()`でソート
- `list`を作成して`heapq.heapify()`でソート
- `heapq.heappush()`でデータを作成しながらソート

<details><summary>実装</summary><div>

```python:sort_ascending.py
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
```
</div></details>
`list`を作成してからheapifyでソートしちゃうのが良い

```text:result
   list:  2.872sec
heapify:  2.302sec
  heapq:  2.543sec
```


# おまけ
### ランダムな位置へのデータ挿入
`list`と`collections.deque`を比較
10万のデータに対して10万回データを追加して比較
Python 3.4.3はdeque.insertがまだ入っていないため，比較実験できていない．
<details><summary>実装</summary><div>

```python:insert_random.py
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
```
</div></details>
Listはworst caseよりかはスコアが良い．

```text:result
 list:  7.268sec
```

### 中央へのデータ挿入
`list`と`collections.deque`を比較
10万のデータに対して10万回データを追加して比較
Python 3.4.3はdeque.insertがまだ入っていないため，比較実験できていない．
<details><summary>実装</summary><div>

```python:insert_mid.py
import timeit
import random
from collections import deque

loop = 10**5
data_size = 10**5
data_range = (1, 10**9)

# list
cmp_list = [random.randint(*data_range) for _ in range(data_size)]
ret_list = timeit.timeit(
    lambda: cmp_list.insert(len(cmp_list)//2, random.randint(*data_range)),
    number=loop)

# # deque
# # randint is not available on Python 3.4.3
# cmp_deque = deque([random.randint(*data_range) for _ in range(data_size)])
# ret_deque = timeit.timeit(
#     lambda: cmp_deque.insert(random.randint(0, len(cmp_deque)), random.randint(*data_range)),
#     number=loop)

print(" list: {:6.3f}sec".format(ret_list))
# print("deque: {:6.3f}sec".format(ret_deque))
```
</div></details>
Listはworst caseよりかはスコアが良い．

```text:result
 list:  7.665sec
```
