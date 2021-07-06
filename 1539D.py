#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()
r=range


n=IN()
a=[0]*n
total=0

for i in range(n):
    aa,bb=LI()
    a[i]=[bb,aa]
    total+=aa
a.sort()

bought=0
bill=0
for item in a:
    if item[0]>bought:
        qntt=min(total-bought,item[0]-bought)
        bought+=qntt
        bill+=(qntt*2)
    qntt=min(total-bought,item[1])
    bought+=qntt
    bill+=qntt
    if bought==total:
        break
print(bill)

