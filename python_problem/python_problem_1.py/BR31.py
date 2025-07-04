import random

def brGame(player, num):
    if player == "computer":
        count = random.randint(1, 3)
        print(f"computer - 부를 숫자의 개수: {count}")
    else:
        while True:
            try:
                count = int(input(f"{player} - 부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
                if count not in [1, 2, 3]:
                    print("1,2,3 중 하나를 입력하세요")
                    continue
                break
            except ValueError:
                print("정수를 입력하세요")
    for i in range(1, count + 1):
        num += 1
        print(f"{player} : {num}")
        if num == 31:
            break
    return num

num = 0
winner = ""

while num < 31:
    num = brGame("computer", num)
    if num == 31:
        winner = "player"
        break
    num = brGame("player", num)
    if num == 31:
        winner = "computer"
        break

print(f"{winner} win!")
