# 概要
Python3にてlist系データの各操作についての処理時間を計測する

# 目的
競技プログラミングでコンテスト中に毎回データ構造を考えており，
時間がもったいないので外部記憶化しておく．
必要な操作から適切なlistを選択できる情報をまとめる．
適宜増やしていく予定

# 前提条件
Python: 3.4.3

## データ参照
### 先頭データの参照
`list`と`collections.deque`と`dict`で比較
10万のデータに対して100万回先頭データへアクセスして比較

[get_first.py](/python/get_first.py)で実装．
先頭の参照は意外とみんな同じくらい

```text
 list:  0.181sec
deque:  0.178sec
 dict:  0.170sec
```

## データ挿入
### 先頭へのデータ挿入
`list`と`collections.deque`を比較
10万のデータに対して10万回データを追加して比較

[insert_first.py](/python/insert_first.py)で実装．
先頭への追加ではdequeを使う方が良い．

```text:result
 list: 12.834sec
deque:  0.226sec
```

### 末尾へのデータ挿入
`list`と`collections.deque`を比較
10万のデータに対して10万回データを追加して比較

[insert_last.py](/python/insert_last.py)で実装．

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

[sort_ascending.py](/python/sort_ascneding.py)で実装．
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
[insert_random.py](/python/insert_random.py)で実装．
Listはworst caseよりかはスコアが良い．

```text:result
 list:  7.268sec
```

### 中央へのデータ挿入
`list`と`collections.deque`を比較
10万のデータに対して10万回データを追加して比較
Python 3.4.3はdeque.insertがまだ入っていないため，比較実験できていない．
[insert_mid.py](/python/insert_mid.py)で実装．
Listはworst caseよりかはスコアが良い．

```text:result
 list:  7.665sec
```
