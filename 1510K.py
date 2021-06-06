#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()


n=IN()
li=LI()

def swap1 (A):
    for i in range(len(A)//2):
        b = A[2*i]
        A[2*i] = A[2*i+1]
        A[2*i+1] = b
    return A

def swap2 (A):
    n = len(A)//2
    for i in range(n):
        b = A[n+i]
        A[n+i] = A[i]
        A[i] = b
    return A

def is_sorted(A):
    for i in range (len(A)):
        if (A[i]!=i+1):
            return False
    return True

if is_sorted(li):
    print(0)
    sys.exit()
ans1=0
ans2=0
li1=li.copy()
li2=li.copy()

while(not (is_sorted(li1)) and (not is_sorted(li2))):
    swap1(li1)
    ans1+=1
    if is_sorted(li1):
        print(ans1)
        break
    swap2(li1)
    ans1+=1
    if is_sorted(li1):
        print(ans1)
        break
    swap2(li2)
    ans2+=1
    if is_sorted(li2):
        print(ans2)
        break
    swap1(li2)
    ans2+=1
    if is_sorted(li2):
        print(ans2)
        break
    if ans1>n:
        print(-1)
        break


