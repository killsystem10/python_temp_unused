import time

print("===계산기===")
time.sleep(1)
a=input("계산을 원하는 첫 정수 입력=")
b=input("계산을 원하는 두번째 정수 입력=")
c=input("계산 방식 입력(+,-,*,/)=")
a=int(a)
b=int(b)
if c=="+":
    result=a+b
    print(result)
elif c=="-":
    result=a-b
    print(result)
elif c=="*":
    result=a*b
    print(result)
elif c=="/":
    result=a/b
    print(result)
else:
    print("오류 발생, 시스템 종료")