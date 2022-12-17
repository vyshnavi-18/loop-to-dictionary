a={'a':500,'b':50,'c':5000,'d':5}
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
        s=i
for i in a:
    if a[i]>max2 and a[i]!=max1 and a[i]!=max:
        max2=a[i]
        k=i
print(d)
print(s)
print(k)