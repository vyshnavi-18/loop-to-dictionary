# dict1={'a':100,'v':200}
# dict2={'n':300,'s':400}
# dict={}
# for d in(dict1,dict2):
#     dict.update(d)
# print(dict)

# a={"a":2,"b":3}
# for i in range(len(a)):
#     print(a[i])

# c={}
# for i in range(5):
#     key=int(input("enter any key"))
#     value=int(input("enter any value"))
#     c[key]=value
# print(c)

a=["mom","sree","maths","dad"]
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if a[i]==[-1]:
            print("polyndrome")
        else:
            print("not polyndrome")
        j=j+1
i=i+1