for t in range(int(input())):
    a,b,k=[int(k) for k in input().split()]
    acl=[int(k) for k in input().split()]
    bcl=[int(k) for k in input().split()]
    ac=[0 for i in range(a)]
    bc=[0 for i in range(b)]
    for i in range(k):
        ac[acl[i]-1]+=1
        bc[bcl[i]-1]+=1
    ans=(k*(k-1))//2
    for i in range(a):
        ans-=(ac[i]*(ac[i]-1))//2
    for j in range(b):
        ans-=(bc[j]*(bc[j]-1))//2
    print(ans)