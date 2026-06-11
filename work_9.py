#if 17
# A,B,C=map(float, input().split())
# if A<B<C or A>B>C:
#     print(A*2,B*2,C*2)
# else:
#     print(A*(-1),B*(-1),C*(-1))
#if 18
# A,B,C=map(float, input().split())
# if A==B>C or A==B<C:
#     print(C)
# elif A==C>B or A==C<B:
#     print(B)
# elif A>B==C or A<B==C:
#     print(C)
# else:
#     print("lidermanov")
# if 19
# A,B,C,D=map(float, input().split())
# if A==B==C>D or A==B==C<D:
#     print(D)
# if A>B==C==D or A<B==C==D:
#     print(A)
# if A==B==D>C or A==B==D<C:
#     print(C)
# if A==D==C>B or A==D==C<B:
#     print(B)
# if 20
# A,B,C=map(int,input().split())
# t1=abs(A-B)
# t2=abs(A-C)
# if t1>t2:
#     print(t2, t1)
# elif t1<t2:
#     print(t1, t2)
# else:
#     print("olg'a Bratan")
#if 21
# x=float(input("x="))
# y=float(input("y="))
# a=float(input("a="))
# if x==y==a==0:
#     print(a)
# elif x==a or y==a:
#     prit(a==1, a==2)
# else:
#     print(a==3)
#if 22
# x=float(input("x="))
# y=float(input("y="))
# a=0
# if x>0 and y>0:
#     print(a==1)
# elif x<0 and y>0:
#     print(a==2)
# elif x<0 and y<0:
#     print(a==3)
# elif x>0 and y<0:
#     print(a==4)
# else:
#     print("Kordinata boshida yotadi")
#if 23
# x1,y1,x2,y2=map(float,input().split())
# A=x1 and y1
# B=x1 and y2
# C=x2 and y2
# D=x2 and y1
# if A and B and C:
#     print(D)
# elif A and B and D:
#     print(C)
# elif A and C and D:
#     print(B)
# else:
#     print(A)
#if 24
# import math
# x=float(input("x="))
# if x>0:
#     print(2*math.sin(x))
# elif x<=0:
#     print(x-6)
# else:
#     print("Assalomu Aleykum")
