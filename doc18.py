dict={'a':65,'b':56,'c':18}
max=0
for i in dict.values():
    if max<i:
        max=i
print(max)

min=i
for i in dict.values():
    if min>i:
        min=i
print(min)