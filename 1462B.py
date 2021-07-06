#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()
r=range


for t in r(IN()):
    n=IN()
    s=S()
    if n<4:
        print("NO")
        continue
    if s[:4]=="2020":
        print("YES")
    elif s[-4:]=="2020":
        print("YES")
    else:
        tar="2020"
        ans=0
        for i in range(4):
            if s[i]==tar[i]:
                ans+=1
            else:
                break
        if ans==4:
            print("YES")
        else:
            rest=4-ans
            tar="0202"
            tar=tar[:rest]
            for i in range(rest):
                if s[n-1-i]==tar[i]:
                    ans+=1
                else:
                    break
            if ans==4:
                print("YES")
            else:
                print("NO")