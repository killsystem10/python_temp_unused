import random
import time
word=['고양이','강아지','호랑이','거북이','개구리','독수리','게','나비','치타','나무늘보','고슴도치']
print("타자 연습 프로그램")
print('10초 이내 단어 5개 입력시 성공')
input("엔터시 시작")

start=time.time()
for i in range(1,6):
    print(i,'번째 문제')
    test=random.choice(word)
    print(test)
    while True:
        type=input()
        if test==type:
            print('성공')
            break
        else:
            print('오타 발생, 다시 도전')
end=time.time()
print('총 시간=',end-start)
if end-start<10:
    print("10초 이내로 성공")
print('프로그램 종료')
