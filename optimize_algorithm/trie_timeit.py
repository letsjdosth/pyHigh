# 속도비교:

import timeit
result_lin = timeit.timeit('trie.test_linear_matches(trie.strings)',
                        setup = 'import trie',
                        number = 10)
print(result_lin) #0.008348800000000045

result_trie = timeit.timeit('trie.test_trie_matches(trie.strings_trie)',
                        setup = 'import trie',
                        number= 10)
print(result_trie) #.00013449999999998186