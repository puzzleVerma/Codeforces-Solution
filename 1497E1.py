#######puzzleVerma#######


import sys
import math
mod = 10**7+1


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()
r=range

fact=[i for i in r(mod)]
for i in reversed(r(2,int(mod**0.5))):
    i=i**2
    for j in range(i,mod,i):
        if fact[j]%i==0:
            fact[j]//=i


for t in r(IN()):
    n,k=LI()
    li=LI()
    div=1
    s=set()
    for ele in li:
        ele=fact[ele]
        if (ele in s):
            div+=1
            s={ele}
        else:
            s.add(ele)
        # print(s)
    print(div)