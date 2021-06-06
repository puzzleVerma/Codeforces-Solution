for t in range(int(input())):
    k,a,b,c=[int(k) for k in input().split()]
    ka=0 if k%a==0 else a-(k%a)
    kb=0 if k%b==0 else b-(k%b)
    kc=0 if k%c==0 else c-(k%c)
    print(min(ka,kb,kc))
