from math import comb
for t in range(int(input())):
    n,k=[int(k) for k in input().split()]
    a=[int(k) for k in input().split()]
    a.sort(reverse=True)
    ele=a[k-1]
    nn=a.count(ele)
    rr=(a[:k]).count(ele)
    print(comb(nn,rr)%(10**9+7))
