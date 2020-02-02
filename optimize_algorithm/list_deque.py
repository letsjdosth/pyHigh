# 파이썬 list는 array-list.
# 따라서 뒤에서 추가/제거하는 작업만 빠름
# 동적으로 동작하지만, 아래에서는 고정 크기 배열이 할당되고 
# 그 할당 슬롯을 넘어서거나 다 갈아엎어야 할 때 메모리 재할당
# 때문에, 뒤에서만 작업하면 재할당이 드물게 일어남.
# 뒤 : 매우 빠름
ex_list = [1 for i in range(30000)]
ex_list.append(1) # ok O(1)
ex_list.pop() # ok O(1)
# 앞
ex_list.insert(0, 1) # 피할 것 O(N)
ex_list.pop(1) # 피할 것 O(N)
# 중간요소를 index로 접근/변경하는 경우는 O(1)로 효율적.
# 중간요소로 값으로 검색시에는 O(N)

# 값으로 검색 시 미리 sorting해두면 좋음.
# 아래 예: 이미 정렬된 리스트에 특정 값 넣을 때, 이진검색으로 추가할 위치를 돌려줌
import bisect
ex1_collection = [1,2,4,5,6]
ex1 = bisect.bisect(ex1_collection, 3) # 찾을 값이 없을 시
print(ex1) #2

ex2_collection = [1,2,3,4,5,6]
ex2_r = bisect.bisect(ex2_collection, 3) # 찾을 값이 이미 있을 시: 오른쪽 인덱스를 알려줌
ex2_l = bisect.bisect_left(ex2_collection, 3) # 찾을 이미 있을 시, bisect_left는 왼쪽 인덱스를 알려줌. 즉 해당 값이 있는 위치를 알려줌.
print(ex2_r,ex2_l) #3 2
# 응용
def index_bisect(given_collection, find_val):
    import bisect
    i = bisect.bisect_left(given_collection, find_val)
    if i != len(given_collection) and given_collection[i] == find_val:
        return i
    else:
        raise ValueError
# 단, 검색은, 정렬과 함께라면 O(log(N)), 정렬된 리스트엔 O(1)이어도, 삽입에는 시간이 오래걸리게(O(N)) 됨.


# 파이썬 deque는 doubly-linked list
# 맨 앞/맨 뒤 모두에서 추가/제거하는 작업을 할 때에 사용

from collections import deque
ex_deque = deque(ex_list)
# 뒤
ex_deque.append(1) # O(1)
ex_deque.pop() # O(1)
# 앞
ex_deque.appendleft(1) # O(1)
ex_deque.popleft() # O(1)
# 그러나 중간요소에 index로 접근하는 연산은 list보다 크게 느림. O(N)
# 중간요소로 값으로 검색시에는 O(N)