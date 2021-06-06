import math
for t in range(int(input())):
    n,k=[int(k) for k in input().split()]
    p=[int(k) for k in input().split()]
    summ=p[0]
    ans=0
    for i in range(1,n):
        if (math.ceil((100*p[i])/k)>summ):
            ans+=((math.ceil((100*p[i])/k))-summ)
            summ+=((math.ceil((100*p[i])/k))-summ)
        summ+=p[i]
    print(ans)