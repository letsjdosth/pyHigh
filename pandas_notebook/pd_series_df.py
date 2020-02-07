import pandas as pd
# 각 자료구조의 바닥 구현은 numpy array임

# pd.Series : key-val map
patients = ["a","b","c","d"]
effective = [True, True, False, False]
effective_series = pd.Series(effective, index=patients)
print(effective_series)
print(effective_series.head)

print(effective_series.loc["a"]) #key 사용시 .loc #True
print(effective_series.iloc[0]) #index number 사용시: .iloc #True
print(effective_series["a"]) #바로 [] 사용 시 key 검색 후 매칭대상 없을 시 index number로 매칭 #true
print(effective_series[0])

# pd.DataFrame : key-{vals} table
columns = {
    "sys_initial" : [120, 126, 130, 115],
    "dia_initial" : [75, 85, 90, 87],
    "sys_final" : [115, 123, 130, 118],
    "dia_final" : [70, 82, 92, 87]
}
df = pd.DataFrame(columns, index=patients)
print(df.head())

#indexing
#행 및 요소 접근
print(df.loc["a"]) #<- return type: pd.Series
print(df.iloc[0]) #<-행 접근됨
print(df.loc["a","sys_initial"])
print(df.iloc[0,0])
#slicing
print(df.iloc[0:2])

#indexing
#열 접근
print(df.sys_initial) #열은 열이름으로 접근가능
print(df["sys_initial"])
print(df[[df.columns[2]]])
print(df.iloc[:,2])
#slicing
print(df.iloc[0:2, 2])


#정렬
#주의: series나 df나 key가 유일성이 보장 안 됨
#pd는 고유키경우/중복키경우(비정렬)/중복키경우(정렬) 에 있어, 접근을 다르게 함
#     O(1)      O(log(N))         O(N)
#고유키를 쓸 것(빠름). 불가피할 중복키에는 정렬할것.
dup_index = list(range(1000)) + list(range(1000))
dupkey_series = pd.Series(range(2000), index=dup_index)
dupkey_series.sort_index(inplace = True) #inplace True:원래 객체를 변화시킴 False: 새 객체를 만들어 반환
print(dupkey_series.head())