for t in range(int(input())):
    s=input()
    if s[0]==s[-1]:
        print("NO")
        continue
    flag=0
    li=[[1,1,-1],[1,-1,1],[-1,1,1],[-1,-1,1],[-1,1,-1],[1,-1,-1]]
    for el in li:
        pr=0
        for ele in s:
            if ele=="A":
                pr+=el[0]
            elif ele=="B":
                pr+=el[1]
            else:
                pr+=el[2]
            if pr<0:
                break
        else:
            if pr==0:
                flag=1
                break
    if flag==1:
        print("YES")
    else:
        print("NO")
    # li=[a,b,c]
    # li.sort()
    # if li[0]+li[1]==li[2]:
    #     print("YES")
    # else:
    #     print("NO")
    # if (s[0]=="A") and (s[-1]=="B") and ((a+c==b) or (b+c==a)):
    #     print("YES")
    #     continue
    # if (s[0]=="A") and (s[-1]=="C") and ((a+b==c) or (b+c==a)):
    #     print("YES")
    #     continue
    # if (s[0]=="B") and (s[-1]=="C") and ((a+c==b) or (b+a==c)):
    #     print("YES")
    #     continue
    # if (s[0]=="B") and (s[-1]=="A") and ((a+c==b) or (b+c==a)):
    #     print("YES")
    #     continue
    # if (s[0]=="C") and (s[-1]=="B") and ((a+c==b) or (b+a==c)):
    #     print("YES")
    #     continue
    # if (s[0]=="C") and (s[-1]=="A") and ((a+b==c) or (b+c==a)):
    #     print("YES")
    #     continue
    # else:
    #     print("NO")
    
    