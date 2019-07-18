import random
import time

word = ["안녕하세요","필통","전화기","마우스","충전기","TV", "지갑", "볼펜"]
n = 1
input("타자게임을 할려면 엔터를 누르세요")
start = time.time()

q = random.choice(word)
while n <= 5:
    print("문제",n)
    print(q)
    x = input()
    if q == x:
        print("통과!")
        n = n+1
        q = random.choice(word)
    else:
        print("오타! 다시 ")

end = time.time()
et = end - start
print("타자시간 : ",et,"초")

