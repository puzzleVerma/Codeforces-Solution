for t in range(int(input())):
    n=int(input())
    s=input()
    ans=""
    ans2=""
    for ele in s:
        if ele=="b":
            ans+=ele
        else:
            ans2+=ele
    print(ans+ans2)