# i=1
# while i<=5:
#     print(i)
#     i=i+1

# i=1
# while i<=5:
#     i=i+1
# print(i)

# i=1
# while i<=5:
#     print(i)
# i=i+1

# i=0
# while i<=5:
#     print(i)
#     i=i-(-1)

# i=105
# while i>=7:
#     print(i)
#     i=i-7
    
# a=int(input("enter any num"))
# i=1
# while i<=10:
#     print(a,"*",i,"=",a*i)
#     i=i+1

# i=0
# while i<=9:
#     i=i+1
#     print(i,i**2)

# i=0
# while i<=5:
#     print(i,i**2)
#     i=i+1

# i=2
# num=int(input("enter num"))
# while i<num:
#     if num%i==0:
#         print(num,"is not a prime num")
#         # break
#     else:
#         print("prime")
#     i=i+1

# **reverse**   
# n=int(input("enter any num"))
# rev=0
# while n!=0:
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# print(rev)

# **series**
# n=int(input("enter any num"))
# i=0
# while i<=n:
#     i=i+1
#     print(1,"/",i,"!","+",end="")


# n=int(input("enter any num"))
# temp=0
# rev=0
# while temp>0:
#     remainder=temp%10
#     temp//=10
#     rev=rev*10+remainder
# if n==rev:
#     print("it is polindrom")
# else:
#     print("it is not a polindrom")


# a=int(input("enter any num"))
# i=2
# fact=0
# while i<a:
#     if a%i==0:
#         fact=fact+1
#     i=i+1
# if fact<=1:
#     print("prime")
# else:
#     print("not a prime")

# string=input("enter")
# i=0
# while i<len(string):
#     j=0
#     while j<=i:  
#         print(string[j],end="")
#         j=j+1
#     print()
#     i=i+1

# string=input("enter")
# i=0
# while i<len(string):
#     j=0
#     while j<=i:
#         print(string[j],end="")
#         j=j+1
#     print()
#     i=i+1
    
    
# **factorial**
# n=int(input("enter"))
# fact=1
# while n>=2:
#     fact=fact*n
#     n=n-1
#     print("factorial",fact)


# # **factorsl** 
# n=int(input("enter"))
# i=0
# while i<=n:
#     i+=1
#     if n%i==0:
#         print(i)


# *fabonicci*
# n=int(input("enter"))
# x=0
# y=1
# z=0
# while x<=n:
#     print(z)
#     x=y
#     y=z
#     z=x+y

# **first few happy numbers are 1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100,** 
# num=int(input("enter a num"))
# sum=0
# while sum!=1 and sum!=4:
# 	sum=0
# 	while num>0:
# 		a=num%10
# 		sum=sum+(a*a)
# 		num=num//10
# 	num=sum
# if sum==1:
# 	print("happy")
# else:
# 	print("sad")



# **harshad**
# n=int(input("enter"))
# sum=0
# a=n
# while a>0:
#     rem=a%10
#     sum=sum+rem
#     a=a//10
#     if (n%sum==0):
#         print(n,"is harshad num")
#     else:
#         print("harsad")

# **armstrong**
# n=int(input("enter a num"))
# a=n
# s=0
# while n>0:
#     s=s+(n%10)*(n%10)*(n%10)
#     n=n//10
# if a==s:
#     print("arm strong")
# else:
#     print("no")
 

# **heart**    
# i=0
# while i<6:
# 	j=0
# 	while j<7:
# 		if (i==0 and j%3!=0) or (i==1 and j%3==0) or (i-j==2) or (i+j==8):
# 			print ("*",end=" ")
# 		else:
# 			print (" ", end=" ")
# 		j=j+1
# 	print ( )
# 	i=i+1

# **diamond**
# i=1
# while i<=5:
# 	b=1
# 	while b<=5-i:
# 		print(" ",end="")
# 		b+=1
# 	j=1
# 	while j<=i:
# 		print("*",end=" ")
# 		j+=1
# 	print()
# 	i+=1
# i=4
# while i>=1:
# 	b=1
# 	while b<=5-i:
# 		print(" ",end="")
# 		b+=1
# 	j=1
# 	while j<=i:
# 		          print("*",end=" ")
# 		j+=1
# 	print()
# 	i-=1

# # **strong num1, 2, 145, and 40585
# s=0
# n=int(input("enter a num"))
# a=n
# while (n):
#     i=1
#     f=1
#     r=n%10
#     while i<=r:
#         f=f*i
#         i+=1
#     s=s+f
#     n=n//10
# if s==a:
#     print("stong num")
# else:
#     print("not")

# n=int(input("enter a num"))
# s=0
# i=1
# while i<n:
#     if n%i==0:
#         s+=i
#     i+=1
# if s==n:
#     print(n,"perfect")
# else:
#     print(n,"not")

# t=int(input())
# for i in range(t):
#     r1,r2,r3=map(int, input().split())
#     if r1+r2<r3 or r2+r3<r1 or r3+r1<r2:
#         print("yes")
#     else:
#         print("no")
    
# def fun():
#     print("hi")
# fun()
# print("bye")
    
# print("hello")
# def fun(a):
#     a=10
#     return(a)
# print(a)
# b=fun(a)
# print(a)
    
# i=1
# while i<=9:
#     j=1
#     while j<=i:
#         print(j%2,end=" ")
#         j=j+1
#     print(i)
#     i=i+1

# k=1
# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(j,end=" ")
#         j=j+1
#         k=k+1
#     print()
#     i=i+1

# a="python"
# i=0
# while i<len(a):
#     j=0
#     while j<=i:
#         print(a[j],end=" ")
#         j=j+1
#     print() 
#     i=i+1

# print("\U0001F618")

n=int(input("enter the num"))
i=0
n=str(n)
while i<len(n):
    if n[i]=='1':
        print("one",end=" ")
    elif n[i]=='2':
        print("two",end=" ")
    elif n[i]=='3':
        print("three",end=" ")
    elif n[i]=='4':
        print("four",end=" ")
    elif n[i]=='5':
        print("five",end=" ")
    elif n[i]=='6':
        print("six",end=" ")
    elif n[i]=='7':
        print("seven",end=" ")
    elif n[i]=='8':
        print("eight",end=" ")
    elif n[i]=='9':
        print("nine",end=" ")
    else:
        print('zero',end=" ")
    i=i+1


        

    
    
    
    
    
    

    
    
    
    
    
    
    

    
    
    

    
    




 