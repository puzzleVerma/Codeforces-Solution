for t in range(int(input())):
    n=int(input())
    b=list(input())
    ans="1"
    pre=int(b[0])+1
    for i in range(1,n):
        if int(b[i])+1==pre:
            pre=int(b[i])
            ans+="0"
        else:
            pre=int(b[i])+1
            ans+="1"
    print(ans)