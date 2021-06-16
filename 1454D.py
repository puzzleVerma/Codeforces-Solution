#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()
r=range


def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while(p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    c = []
    for p in range(2, n):
        if prime[p]:
            c.append(p)
    return c

def prime(n):
    if n<2:
        return False
    if n==2:
        return True
    if (n>2 and n%2==0):
        return False
    ans=True
    for i in range(3,int(n**0.5+1),2):
        if n%i==0:
            ans=False
            break
    return ans




pn=SieveOfEratosthenes(10**5)    



for t in r(IN()):
    n=IN()
    if prime(n):
        print(1)
        print(n)
        continue
    ans=0
    for ele in pn:
        temp=0
        nn=n
        if nn%ele==0:
            while (nn%ele==0):
                temp+=1
                nn//=ele
            if temp>ans:
                pri=ele
                lst=nn
                ans=temp

    res=[pri]*ans
    res[-1]*=lst
    print(ans)
    print(*res)

    # pf=primeFactors(n)
    # ans=[pf[0]]
    # for i in range(1,len(pf)):
    #     if pf[i]%ans[-1]==0:
    #         ans+=[pf[i]]
    # print(len(ans))
    # print(*ans)
    