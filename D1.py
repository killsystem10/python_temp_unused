first=0
second=0
a=0
b=0
c=0
a_count=0
b_count=0
c_count=0

first=int(input())
second=int(input())
a, b, c =input().split()
a=int(a)
b=int(b)
c=int(c)
have=first-second

if a>b>c:
    while True:
        if have-a<0:
            break
        else:
            have=have-a
            a_count=a_count+1
            continue
    while True:
        if have-b<0:
            break
        else:
            have=have-b
            b_count=b_count+1
            continue
    while True:
        if have-c<0:
            break
        else:
            have=have-c
            c_count=c_count+1
            continue
if a>c>b:
    while True:
        if have-a<0:
            break
        else:
            have=have-a
            a_count=a_count+1
            continue
    while True:
        if have-c<0:
            break
        else:
            have=have-c
            c_count=c_count+1
            continue
    while True:
        if have-b<0:
            break
        else:
            have=have-b
            b_count=b_count+1
            continue
if b>a>c:
    while True:
        if have-b<0:
            break
        else:
            have=have-b
            b_count=b_count+1
            continue
    while True:
        if have-a<0:
            break
        else:   
            have=have-a
            a_count=a_count+1
            continue
        while True:
            if have-c<0:
                break
            else:   
                have=have-c
                c_count=c_count+1
                continue
if b>c>a:
    while True:
        if have-b<0:
            break
        else:
            have=have-b
            b_count=b_count+1
            continue
    while True:
        if have-c<0:
            break
        else:
            have=have-c
            c_count=c_count+1
            continue
    while True:
        if have-a<0:
            break
        else:
            have=have-a
            a_count=a_count+1
            continue
if c>a>b:
    while True:
        if have-c<0:
            break
        else:
            have=have-c
            c_count=c_count+1
            continue
    while True:
        if have-a<0:
            break
        else:
            have=have-a
            a_count=a_count+1
            continue
    while True:
        if have-b<0:
            break
        else:
            have=have-b
            b_count=b_count+1
            continue
if c>b>a:
    while True:
        if have-c<0:
            break
        else:
            have=have-c
            c_count=c_count+1
            continue
    while True:
        if have-b<0:
            break
        else:
            have=have-b
            b_count=b_count+1
            continue
    while True:
        if have-a<0:    
            break
        else:
            have=have-a
            a_count=a_count+1
            continue
sum=a_count+b_count+c_count
if have==0:
    print(sum)
else:
    print(-1)

