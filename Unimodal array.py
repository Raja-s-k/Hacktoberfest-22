a=int(input())
b=list(map(int,input().split()))
c=max(b)

if b.count(c) == len(b):
    print("YES")
elif b.count(c) == 1:
    
    if b[-1] == c:
        b.append(c+1)

    if b[b.index(c)]>b[b.index(c)+1] and b[b.index(c)]>b[b.index(c)-1]:
        print("YES")
    else:
        print("NO")
elif b.count(c) > 1 and b[b.index(c)]!=b[b.index(c)+1]:
    print("NO")
elif b.count(c) > 1 and b[:b.index(c)].count(b[b.index(c)-1])>1:
    print("NO")
elif b.count(c) > 1 and b[0]== c and b[-1]== c:
    print("NO")
elif b.count(c) > 1 and b.count(c)!=b[:b.index(b[-1])].count(c):
    
    for i in range(b.count(c)-1):
        if b[b.index(c)]!=b[b.index(c)+1]:
            break
        else:
            b.remove(c)
        
    b.remove(c)
    
    if b[b.index(c)]>b[b.index(c)-1] and b[b.index(c)]>b[b.index(c)+1]:
        print("YES")
    else:
        print("NO")


elif b.count(c) > 1 :
    for i in range(b.count(c)-1):
        b.remove(c)
        
    if b[b.index(c)]>b[b.index(c)-1] or b[b.index(c)]>b[b.index(c)+1]:
        print("YES")
    else:
        print("NO")

