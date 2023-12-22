import time
import random
right=0
fall=0
print("====숫자 빨리치기====")
temp=input("엔터시 시작")
firsttime=time.time()
for i in range(10):
    word=random.randint(0,9)
    print(word
          )
    while True:
        answer=input("숫자 입력=")
        answer=int(answer)
        if answer==word:
            print("정답")
            right=right+1
            break
        else:
            print("틀림, 다시시도")
            fall=fall+1
            continue
secondtime=time.time()
finaltime=secondtime-firsttime
print("맞은 횟수="+str(right), "틀린 횟수="+str(fall), "걸린시간="+str(finaltime))


