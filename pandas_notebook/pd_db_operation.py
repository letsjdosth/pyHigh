import pandas as pd
import numpy as np

# pd 바닥이 np array이므로, array 연산이 다 지원됨
# 단, key-val 요소는 같은 키값끼리 연산된다는것만 주의

a = pd.Series([1,2,3], index=["a","b","c"])
b = pd.Series([4,5,6], index=["a","b","c"])
c = pd.Series([7,8,9], index=["a","b","d"])

print(np.log(a))
print(a ** 2)

print(a+b)
print(a+c) #주의. 일치하지 않는 키는
# a     8.0
# b    10.0
# c     NaN #<- -_-Nan을 뱉어버린다
# d     NaN 
# dtype: float64


# 함수형 연산
patients = ["a","b","c","d"]
columns = {
    "sys_initial" : [120, 126, 130, 115],
    "dia_initial" : [75, 85, 90, 87],
    "sys_final" : [115, 123, 130, 118],
    "dia_final" : [70, 82, 92, 87]
}
df = pd.DataFrame(columns, index=patients)
def superstar(x):
    return "*" + str(x) + "*"
print(a.map(superstar)) #map (for series)
print(df.applymap(superstar)) #map (for df)
print(df.apply(superstar, axis=0)) #axis는 행에 적용


#numexpr 이용 연산: eval
print(df.eval("sys_final - sys_initial")) #인스턴스의 메소드이므로, key(열명)을 곧바로 사용가능
df_delta = df.eval("sys_delta = sys_final - sys_initial", inplace=False)
print(df_delta)
#    sys_initial  dia_initial  sys_final  dia_final  sys_delta
# a          120           75        115         70         -5
# b          126           85        123         82         -3
# c          130           90        130         92          0
# d          115           87        118         87          3