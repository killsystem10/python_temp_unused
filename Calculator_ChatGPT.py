print("간단한 계산기 프로그램입니다.")
num1 = float(input("첫번째 수를 입력하세요: "))
operator = input("연산자를 입력하세요 (+, -, *, /): ")
num2 = float(input("두번째 수를 입력하세요: "))

if operator == '+':
    result = num1 + num2
    print(num1, "+", num2, "=", result)
elif operator == '-':
    result = num1 - num2
    print(num1, "-", num2, "=", result)
elif operator == '*':
    result = num1 * num2
    print(num1, "*", num2, "=", result)
elif operator == '/':
    if num2 == 0:
        print("0으로 나눌 수 없습니다.")
    else:
        result = num1 / num2
        print(num1, "/", num2, "=", result)
else:
    print("잘못된 연산자입니다.")
