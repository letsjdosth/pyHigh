import numpy as np
import pandas as pd

patients = ["a","b","c","d","e","f"]
columns = {
    "sys_initial" : [120, 126, 130, 115, 150, 117],
    "dia_initial" : [75, 85, 90, 87, 90, 74],
    "sys_final" : [115, 123, 130, 118, 130, 121],
    "dia_final" : [70, 82, 92, 87, 85, 74],
    "drug_admst" : [True, True, True, True, False, False]
}
df = pd.DataFrame(columns, index=patients)

# grouping
# df.groupby -> group기준값,group내해당df열 로 묶인 객체 반환(인스턴스는 자체타입이긴함)
for value, group in df.groupby("drug_admst"):
    print("Value: {}".format(value))
    print("Group DataFrame:")
    print(group)
# Value: False
# Group DataFrame:
#    sys_initial  dia_initial  sys_final  dia_final  drug_admst
# e          150           90        130         85       False
# f          117           74        121         74       False
# Value: True
# Group DataFrame:
#    sys_initial  dia_initial  sys_final  dia_final  drug_admst
# a          120           75        115         70        True
# b          126           85        123         82        True
# c          130           90        130         92        True
# d          115           87        118         87        True


# calculation on group
# agg() : aggregation
print(df.groupby('drug_admst').agg(np.mean))
#             sys_initial  dia_initial  sys_final  dia_final
# drug_admst
# False            133.50        82.00      125.5      79.50
# True             122.75        84.25      121.5      82.75

# transform() : 전체에 대상함수 적용
df.loc['a','sys_initial'] = None
print(df.groupby('drug_admst').transform(lambda df: df.fillna(df.mean())))
#<-연쇄로 쓸 수 있음. None값을 group mean으로 채움


# join
hospitals = pd.DataFrame(
    {
        "name" : ["City1", "City2", "City3"],
        "address" : ["Address1", "Address2", "Address3"],
        "city" : ["City1", "City2", "City3"]
    }, index=["H1", "H2", "H3"]
)
print(hospitals)

hospital_id = ["H1", "H2", "H2", "H3", "H3", "H3"]
df['hospital_id'] = hospital_id
print(df)

# simply
cities = hospitals.loc[hospital_id, "city"]
print(cities)

# or use pd.join
result = df.join(hospitals, on="hospital_id") #df에 hospitals를, left join
print(result)

