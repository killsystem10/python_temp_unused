n=m=a=b=c=h=j=i=k=0
n=int(input())
m=int(input())
k=list(map(int, input().split()))
k.sort()
h=n-m
a=int(k[0])
b=int(k[1])
c=int(k[2])

while True:
    if h==0:
       print(i)
       break 
    if h-c<0:
        if h-b<0:
            if h-a<0:
                print(-1)
                break
            else:
                i+=1
                h-=a    
        else:
            i+=1
            h-=b
    else:
        i+=1
        h-=c
