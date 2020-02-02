# heap
# 알고리즘 자체는 이진트리 기반.
# 구현 하부는 리스트(array list)

# 최대/최소값 접근에 유용 O(log(N)) <> list: 미정렬시 O(log(N)), 정렬시 O(1)
# 또한 삽입도 O(log(N)) <> list: O(N)

import heapq

collection = [10, 3, 3, 4, 5, 6]
heapq.heapify(collection)

# 최소값 추출
minval = heapq.heappop(collection) #O(log(N))
print(minval) #3

# 최대값 추출 : -1을 붙이고 힙을 만든다.
minus_collection = [-val for val in [10,3,3,4,5,6]]
heapq.heapify(minus_collection)
maxval = - heapq.heappop(minus_collection)
print(maxval) #10

# 값 삽입
heapq.heappush(collection, 1) #O(log(N))
print(collection) #[1, 4, 3, 10, 5, 6]




# heap의 다른 간단한 대안: PriorityQueue
# 스레드/프로세스에 안전함
from queue import PriorityQueue

queue = PriorityQueue()
for element in collection:
    queue.put(element)
minval_from_PQ = queue.get()
print(minval_from_PQ) #1


# ex1. task들에 우선순위 설정
# idea: (priority(작을수록 우선), task객체) 를 이용
task_queue = PriorityQueue()
task_queue.put((3, "priority 3"))
task_queue.put((2, "priority 2"))
task_queue.put((1, "priority 1"))
highest_priority_task = task_queue.get()
print(highest_priority_task) #(1, 'priority 1')