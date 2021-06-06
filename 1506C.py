#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()


for t in range(IN()):
    a=S()
    b=S()
    i=0
    j=0
    maxsame=0
    same=0
    while i<len(a):
        ist=i
        while j<len(b):
            if a[i]==b[j]:
                i+=1
                j+=1
                same+=1
            elif (a[i]!=b[j] and i!=ist):
                maxsame=max(maxsame,same)
                j-=same
                j+=1
                same=0
                i=ist
            else:
                j+=1
            if (i>=len(a) or j>=len(b)):
                break
        i=ist   
        i+=1
        j=0
        maxsame=max(maxsame,same)
        same=0
    print(len(a)+len(b)-maxsame-maxsame)