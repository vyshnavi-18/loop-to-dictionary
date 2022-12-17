# person= {'1': 'vaishu', '2': 17,}
# person[3] = 'female'
# print(person)

# details={
# 'Name': 'ANAND',
# 'Age': 17, 
# 'student': {
# 'id': 22,
# 'place': 'ANANTAPUR'
# }
# } 
# details['student']['id']=35
# print(details);

# a={"sree":7,"A":8,"B":9,"C":10}
# a.update({"A":10}) 
# a.update({"C":11})
# print(a)

a={'1','2','3','4','5'}
b=[1,2,3,4,5]
for i in a:
    for j in b:
        c=dict.fromkeys({a[i],b[j]})
print(c)

