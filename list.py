# # # # a=[1,2,3]
# # # # a.append(4)
# # # # print(a)

# list=[1,2,3,4,5,6,7,8,9,12,34,56,78,90,]
# k=4
# a=[]
# i=0
# while i<len(list):
#     if i==k:
#         a.append(20)
#         k=k+4
#     a.append(list[i])
#     i=i+1
# # print(a)       

# # a=int(input("enter how many rows"))
# # list=[]
# # while a>=1:
# #     item=input("enter any thing")
# #     list.append(item)
# #     a=a-1
# # print(list)     

# a=["anand","vaishnavi","nandhu"] 
# i=0
# b=[]
# while i<len(a):
#     b.append(list(a[i]))
#     i=i+1
# print(b)
 
# a=[10,110,1100,1000]
# i=0
# l=[]
# while i<len(a):
#     b=str(a[i])
#     if '0'in b:
#         l.append((b.replace("0"," ")))
#     i+=1   
# print(l)

# a=[1,2,3,4]
# i=0
# sum=0
# while i<len(a):
#     sum=sum+a[i]
#     i=i+1
# print(sum)

# num=[50,40,23,70,56,12,5,10,71]
# count=0
# i=0
# while i<len(num):
#     if 20<=num[i]<=40:
#         count=count+1
#     i=i+1 
# print(count)
       
# a=[[1,2,3],[4,5,6,],[7,8,9]]
# i=0
# b=0
# while i<len(a):
#     sum=0
#     j=0
#     while j<len(a[i]):
#         sum=sum+a[i][j]
#         j=j+1
#     i=i+1
# print(sum)

# a=[5,4,[6,2],3,9]
# i=0
# b=0
# while i<len(a):
#     sum=0
#     j=0
#     while j<len(a[i]):
#         sum=sum+a[i][j]
#         j=j+1
#     i=i+1
# print(sum)


# n=["m","o","m"]
# b=[]
# i=1
# while i<len(n):
#     b.append(n[-i])
#     i=i+1
# print(b)
# if b==n:
#     print("it is polindrom")
# else:
#     print("it is not polindrom")


# a=[1,2,[1,2],[3,4],1,2]
# i=0
# sum=0
# while i<len(a):
#     if type(a[i])==list:
#       j=0
#       while j<len(a[i]):
#         sum=sum+a[i][j]
#         j=j+1
#     else:
#         sum=sum+a[i]
#     i=i+1
# print(sum)    
    
# a="anandvaishu"
# b=[]
# i=0
# while i<len(a):
#     b.append(a[i])
#     b.append((i+1)*len(a))
#     i=i+1
# print(b)  

# a=(1,2,3,4,5)
# b=[]
# b.append a[6]
# # print(b)

# a=[2,4,5,2,3,2,2]
# i=0
# b=[]
# while i<len(a):
#     if a[i]!=2:
#         b.append (a[i])
#     i=i+1
# print(b)

# a="ptthon"
# i=0
# b=input("enter any thing")
# c=[]
# while i<len(a):
#     if a[i]=="b":   
#        c.append(b)
#     else:
#         c.append(a[i])
#     i=i+1
# print(c)
 
# a=[1,2,3,4,5,6,7]
# b=a[-3:3:-1]
# print(b)

# a=[2,3,4,5,6]                                         
# i=0
# b=""
# while i<len(a):
#     b=b+str(a[i]*2)   
#     i=i+1
# print(b) 
   
# a=[2,2,3,4,5,6]
# a.remove(2)
# print(a)

# a=[2,3,4,5,8,9]
# b=[] 
# b.access(a[3])
# print(b)


# num=input("enter your name:")
# if num>="a" and num<="z":
#     print("sun")
#     age=int(input("enter your age:"))
#     if age>0:
#         print("18")
#     else:
#         print("wrong")
# else:
#     print("wrong2")
    
# n=int(input("enter any number:"))
# while n<=100:
#     c=0
#     i=2
#     while i<=n//2: 
#         if n%i==0:
#             c+=1
#             break
#         i+=1
#     else:
#         print(n)
#     n+=1
        
# a=[1,0,5,7,0,0,3]
# b=[]
# c=[]
# i=0
# while i<len(a):
#     if a[i]==0:
#         b.append(a[i])                                           
#     else:
#         c.append(a[i])
#     i+=1
# c.extend(b)
# print(c)

# a=int(input("enter any num"))
# i=0
# b=[]
# while i<a:
#     num=int(input("enter the num"))
#     b.append(num)
#     i=i+1
# print(b)


# a=[4,5,6,3,9,5]
# i=0
# sum=0
# # while i<len(a):
# #     sum=sum+a[i]
# #     i=i+1
# # print(sum)


# # a=int(input("enter any num"))
# # i=0
# # b=[]
# # count=0
# # while i<(a):
# #     num=int(input("enter any num"))
# #     if i%3==0:
# #         count=count+1
# #     i=i+1
# # print(count)

# i=1
# while i<6:
#     b=1
#     while b<=6-i:
#    j=1
#     while j<=i:
#         print(j,end=" ")
#         j+=1
#     m=1
#     while m<i:
#         print(i-m,end=" ")
#         m+=1
#     print()
#     i+=1
#       print(" ",end=" ")
#         b+=1
   

# a=int(input("enter any num"))
# b=int(input("enter any num"))
# i=0
# s=0
# while i<=a:
#     s=s+b
#     i=i+1
# print(s)

# a=[4,5,6,7,9,2,1]
# i=0
# sum=0
# pr=0
# while i<=a:
#     # sum=sum+a[i][0][4]
#     # pr=pr*a[i][4][6]
#     i=i+1
# print(sum)
# print(pr)

# a=["my5","name10","vaishu15"]
# i=0
# b=[]
# sum=" "
# while i<len(a):
#     j=0
#     s=" "
#     while j<len(a[i]):
#         if a[i][j]>="a" and a[i][j]<="z":           
#             sum=sum+a[i][j]
#         j=j+1
#     b.append(sum)
# print(b)

# a="vaishnavi"
# i=0
# while i<len(a):
#     j=0
#     while j<=i:
#         print(a[j],end="")
#         j=j+1
#     # i=i+1
# print()
# i=i-1

# a="vaishnavi"
# i=0
# while i>=9:
#     j=0
#     while j<=i:
#         print(i,end=" ")
#         j=j+1
#     print()
#     i=i+1
        
# i=5
# while i>=1:
#     j=1
#     while j<=i:
#         print(i,end=" ")
#         j=j+1
#     print()
#     i-=1

# a=[4,5,6,7,]
# b=[7,6,5,4]
# i=0
# u=[]
# while i<len(a):
#     c=a[i]+b[i]
#     u.append(a[i]+b[i])
#     i=i+1
# print(u)

# a="890503005"
# i=0
# b=a
# while i<len(a):
#     if a==0:
#         b.append(a(i))
#         i=i+1
# # print(b)

# a="890503005"
# i=0
# b=a
# while i<len(a):
#     if "0" in b:
#         b.remove (a(0))
#         i=i+1
# print(b)


