dt={1:2,3:4,4:3,2:1,0:0}
# sorted_dt = {key: value for key, value in sorted(dt.items(), key=lambda item: item[1])}
# print(sorted_dt)
# sorted_dt = {key: value for key, value in reversed(sorted(dt.items(), key=lambda item: item[1]))}
# print(sorted_dt)
d=sorted([(value,key)
for (key,value) in dt.items()])
print(d)
e=reversed([(keys,values)
for(values,keys) in dt.items()])
print(e)
