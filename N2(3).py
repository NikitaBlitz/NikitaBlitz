A=['a','b']
P=str(input())
k=len(P)
f=0
for i in range(1,k):
    if P[i] not in A:
        f=0
        break
    else:
        f=1
if f==0:
    print("В вашей строке есть символ, которого нет в алфавите")
else:
    x=P.count('a')
    y=P.count('b')
    print('a'*x+'b'*y)


    