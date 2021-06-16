#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()
r=range

al="abcdefghijklmnopqrstuvwxyz"
for t in r(IN()):
    n=IN()
    s=S()
    flag=0

    while 1:
        for i in r(26):
            if al[i] not in s:
                print(al[i])
                flag=1
                break
        if flag==1:
            break
        for i in r(26):
            if flag==1:
                break
            for j in r(26):
                sr=al[i]+al[j]
                if sr not in s:
                    print(sr)
                    flag=1
                    break
        if flag==1:
            break
        for k in r(26):
            if flag==1:
                break
            for i in r(26):
                if flag==1:
                    break
                for j in r(26):
                    sr=al[k]+al[i]+al[j]
                    if sr not in s:
                        print(sr)
                        flag=1
                        break
        if flag==1:
            break
