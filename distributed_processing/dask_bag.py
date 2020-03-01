# dask.bag
# Dask Bag implements operations like map, filter, fold, and groupby on collections of generic Python objects. 
# It does this in parallel with a small memory footprint using Python iterators. 
# It is similar to a parallel version of PyToolz or a Pythonic version of the PySpark RDD.

# python multiprocessing/threading standard library 의존

import dask.bag as dab

b = dab.from_sequence(range(40), npartitions=4)

print(b)
#dask.bag<from_sequence, npartitions=4>

print(dict(b.dask))
# {('from_sequence-5852f8b7c56272476c57f89cdcfcb890', 0): [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
# ('from_sequence-5852f8b7c56272476c57f89cdcfcb890', 1): [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 
# ('from_sequence-5852f8b7c56272476c57f89cdcfcb890', 2): [20, 21, 22, 23, 24, 25, 26, 27, 28, 29], 
# ('from_sequence-5852f8b7c56272476c57f89cdcfcb890', 3): [30, 31, 32, 33, 34, 35, 36, 37, 38, 39]}


# ex : word counting
if __name__=="__main__":
    collection = dab.from_sequence(["the cat sat on the mat", "the dog sat on the mat"], npartitions=2)
        
    def binop(total, x):
        # reduce func
        return total + x["count"]
    def combine(a,b):
        return a+b

    
    res = (collection
        .map(str.split)
        .flatten()
        .map(lambda x: {"word" : x, "count" : 1})
        .foldby(lambda x: x["word"], binop, 0, combine, 0)
        .compute()
    )
    # foldby(key, binop, initial='__no__default__', combine=None, combine_initial='__no__default__', split_every=None)
    # Combined reduction and groupby.
    print(res)
    # [('the', 4), ('cat', 1), ('sat', 2), ('on', 2), ('mat', 2), ('dog', 1)]