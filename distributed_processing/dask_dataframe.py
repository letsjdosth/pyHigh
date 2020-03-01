# dask.dataframe
# A Dask DataFrame is a large parallel DataFrame composed of many smaller Pandas DataFrames, split along the index.
# These Pandas DataFrames may live on disk for larger-than-memory computing on a single machine, 
# or on many different machines in a cluster

# numpy array -> pandas dataframe에 의존

import dask.dataframe as dd
import dask.bag as dab

if __name__=="__main__":
    collection = dab.from_sequence(
        ["the cat sat on the mat",
         "the dog sat on the mat",
         "the cat run in the room",
         "Mimi sleeped on the mat"], npartitions=2)
    
    words = (collection
        .map(str.split)
        .flatten()
    )
    df = words.to_dataframe([('words','str')])
    print(df)
    print(df.head())

    res = df.words.value_counts().compute() #알아서 병렬처리함
    print(res)
    # the        7
    # on         3
    # mat        3
    # sat        2
    # cat        2
    # sleeped    1
    # run        1
    # room       1
    # in         1
    # dog        1
    # Mimi       1
    # Name: words, dtype: int64