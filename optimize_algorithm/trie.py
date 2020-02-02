# trie
# 파이썬 standard library에는 없음
# https://en.wikipedia.org/wiki/Trie
# 문자열 검색을 위해 트리를 특화

from random import choice
from string import ascii_uppercase

from patricia import trie

def random_string(length):
    # ascii 대문자 셋에서 랜덤으로 length개를 뽑아 붙여 string을 리턴
    return ''.join(choice(ascii_uppercase) for i in range(length))

strings = [random_string(32) for i in range(10000)]
# print(strings[0:2])


# ex1. AA로 시작하는 문자?
# 비교 케이스: 선형 검색시
def test_linear_matches(strings):
    return [s for s in strings if s.startswith('AA')]

# trie 사용시
strings_dict = {s:0 for s in strings}
strings_trie = trie(**strings_dict)
def test_trie_matches(strings_trie):
    return list(strings_trie.iter('AA'))

# 속도비교: trie_timeit.py 실행