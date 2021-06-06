for t in range(int(input())):
    n=int(input())
    s=input()
    if ((s[0]=="0") or (s[-1]=="0")):
        print("NO")
        continue
    else:
        z=0
        for i in range(n):
            if s[i]=="0":
                z+=1
        if (z%2):
            print("NO")
        else:
            print("YES")
            a=["0"]*n
            b=["0"]*n
            a[0]="("
            b[0]="("
            a[-1]=")"
            b[-1]=")"
            ao=0
            az=0
            for i in range(1,n-1):
                if s[i]=="0":
                    if (az):
                        a[i]=")"
                        b[i]="("
                        az=0
                    else:
                        a[i]="("
                        b[i]=")"
                        az=1

                    
                else:
                    if (ao):
                        a[i]=")"
                        b[i]=")"
                        ao=0
                    else:
                        a[i]="("
                        b[i]="("
                        ao=1

            print(''.join([i for i in a]))
            print(''.join([i for i in b]))
                
            