# dict=int(input("enter any num"))
# dict={""}
# c=0
# print([dict])

# str1 = 'w3resource' 
# my_dict = {}
# for letter in str1:
#     my_dict[letter] = my_dict.get(letter, 0) + 1
# print(my_dict)

# a="w3resource"
# b={}
# for i in a:
#     if i in b:
#         b[i]+=1
#     else:
#         b[i]=1
# print(b)

# a = {}
# for i in my_dictionary:
    # if i%2==0:
        # i=i+1
# print(my_dictionary)
a={}
c=[]
for i in a:  
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
