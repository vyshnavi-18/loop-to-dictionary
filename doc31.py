a={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55,
'item5': 24}
max=0
max1=0
max2=0
for i in a:
    if a[i]>max:
        max=a[i]
        d=i
for i in a:
    if a[i]>max1 and a[i]!=max:
        max1=a[i]
        b=i
for i in a:
    if a[i]>max2 and a[i]!=max1 and a[i]!=max:
        max2=a[i]
        c=i
print(d,max)
print(b,max1)
print(c,max2)