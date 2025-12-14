try:
    n,k=map(int,input().split(' '))
    if k>1e6:
        print("No")
    else:
        s=set()
        ok=True
        for i in range(1,int(k)+1):
            r=n%i
            if r in s:
                ok=False
                break
            s.add(r)
        if ok:
            print("Yes")
        else:
            print("No")
except:
    print("No")
