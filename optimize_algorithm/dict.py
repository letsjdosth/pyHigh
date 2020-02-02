# dict
# hashmap으로 구현.
# 요소 삽입/삭제/접근 모두 O(1)
# 단, 구현체의 해시함수 자체가 빨라야 / 충돌이 많이 없고 충돌시 제어가 필요. 
# (standard lib은 충분히 빠른 듯)

# ex1. 리스트의 각 요소 세기
def counter_dict(items): # O(N)
    counter = {}
    for item in items:
        if item not in counter:
            counter[item] = 1
        else:
            counter[item] += 1
    return counter

from collections import defaultdict
def counter_defaultdict(items): # O(N)
    counter = defaultdict(int)
    for item in items:
        counter[item] += 1
    return counter

from collections import Counter # O(N)

ex_list = [1,3,2,5,6,3]
print(counter_dict(ex_list)) # {1: 1, 3: 2, 2: 1, 5: 1, 6: 1}
print(counter_defaultdict(ex_list)) # defaultdict(<class 'int'>, {1: 1, 3: 2, 2: 1, 5: 1, 6: 1})
print(Counter(ex_list)) # Counter({3: 2, 1: 1, 2: 1, 5: 1, 6: 1})
# 모두 O(N)이긴 하지만 Counter가 가장 빠름. 다음 counter_dict, 그다음 counter_defaultdict. 내부적으로 더 최적화되어 있는 듯


# ex2. 리스트 역색인 구축
docs = ["the cat is under the table",
    "the dog is under the table",
    "cats and dogs smell roses",
    "Carla eats an apple"]

# 색인 없이 검색시 : O(N)
noindex_matchs_table = [doc for doc in docs if "table" in doc]
print(noindex_matchs_table) #['the cat is under the table', 'the dog is under the table']

# 색인 이용시
index={}
for i, doc in enumerate(docs):
    for word in doc.split():
        if word not in index:
            index[word] = [i]
        else:
            index[word].append(i)
print(index)
# {'the': [0, 0, 1, 1], 'cat': [0], 'is': [0, 1], 'under': [0, 1], 'table': [0, 1],
#  'dog': [1], 'cats': [2], 'and': [2], 'dogs': [2], 'smell': [2], 'roses': [2],
#   'Carla': [3], 'eats': [3], 'an': [3], 'apple': [3]}
index_matches_table_idx = index['table']
print(index_matches_table_idx) # [0, 1]
index_matches_table = [docs[i] for i in index_matches_table_idx]
print(index_matches_table) # ['the cat is under the table', 'the dog is under the table']

# 색인 구축은 오래걸리나 이건 1회만 하면 됨. 이후 검색은 O(1)으로 매우 고속으로 가능


