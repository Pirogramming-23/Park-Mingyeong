num = 0
winner = ""  # 승자 저장

while num < 31:
    # playerA 차례
    while True:
        try:
            count = int(input("playerA - 부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
            if count not in [1, 2, 3]:
                print("1,2,3 중 하나를 입력하세요")
                continue
            break
        except ValueError:
            print("정수를 입력하세요")
    for i in range(1, count + 1):
        num += 1
        print(f"playerA : {num}")
        if num == 31:
            winner = "playerB"
            break
    if num == 31:
        break

    # playerB 차례
    while True:
        try:
            count = int(input("playerB - 부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
            if count not in [1, 2, 3]:
                print("1,2,3 중 하나를 입력하세요")
                continue
            break
        except ValueError:
            print("정수를 입력하세요")
    for i in range(1, count + 1):
        num += 1
        print(f"playerB : {num}")
        if num == 31:
            winner = "playerA"
            break
    if num == 31:
        break

# 승자 출력
print(f"{winner} win!")
