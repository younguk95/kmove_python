import random,time


input(" 게임 시작")
t1 = time.time()

def make_question():
    a = random.randint(1,40)
    b = random.randint(1,20)
    op = random.randint(1,3)
  
    
    q =str(a)

    if op == 1:
        q = q + "+"
    if op == 2:
        q == q + "-"
    if op == 3:
        q == q + "*"
    if op == 4:
        q == q + "/"
    
    q = q + str(b)

    return q
  
   

sc1 = 0
sc2 = 0

for x in range(5):
    q = make_question()
    print(q)
    ans = input("=")
    r = int(ans)

    if eval(q) == r:
        print("정답")
        sc1 = sc1 + 1
    else:
        print("오답")
        sc2 = sc2 + 1
    print("정답 : " ,sc1, "오답",sc2)

t2 = time.time()
et = t2 - t1
print("%.0f초동안 %d개 맞음" %(t2-t1))
    
   





