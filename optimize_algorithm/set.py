# set
# hash로 구현 (dict key만 뗀 것)
# 추가/삭제/접근/소속여부검사 모두 O(1)

# list->set 변환 복잡도: O(N)
# 중복제거시 전체 list를 다 보긴 해야 하기 때문
x = list(range(1000)) + list(range(500))
x_unique = set(x) # O(N)

# set 연산 복잡도
s = {1,2,3,4,5}
t = {4,5,6,7}
s.union(t) #O(5+4) (O(S+T))
s.intersection(t) # O(4) (O(min(S,T)))
s.difference(t) # O(5) (O(S))

# ex1 : 복수단어 색인 질의
docs = ["the cat is under the table",
    "the dog is under the table",
    "cats and dogs smell roses",
    "Carla eats an apple"]
index = {}
index={}
for i, doc in enumerate(docs):
    for word in doc.split():
        if word not in index:
            index[word] = {i} #<-여기에 list대신 set을 쓰자
        else:
            index[word].add(i)

match_cat_and_table_idx = index['cat'].intersection(index['table'])
match_cat_and_table = [docs[i] for i in match_cat_and_table_idx]
print(match_cat_and_table) #['the cat is under the table']
