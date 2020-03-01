from operator import add

import dask

directed_acyclic_graph = {
    "a" : 2,
    "b" : 2,
    "result" : (add, "a", "b")
}

res = dask.get(directed_acyclic_graph, "result")
print(res)