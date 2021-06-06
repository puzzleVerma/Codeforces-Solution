#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()


n=IN()
li=[]
pro=1
for i in range(1,n):
    if math.gcd(n,i)==1:
        li.append(i)
        pro*=i
        pro%=n
if pro!=1:
    li.remove(pro)
print(len(li))
print(*li)