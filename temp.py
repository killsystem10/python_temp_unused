preh=2
nexh=3
battery=0



if preh>nexh:
    temp=preh-nexh
    battery=2*temp
elif preh<nexh:
    temp=nexh-preh
    temp=temp/2
