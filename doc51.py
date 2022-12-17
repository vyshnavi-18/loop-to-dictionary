a={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
b=[]
c=[]
for i in a.values():
    for j in i:
        c.append(j)
        k=0
        d=[]
        while k<len(a):
            if c[k]%2==0:
                d.append(c[k])
            k=k+1
print(d)
