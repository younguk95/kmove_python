import random
import time


word = ["안녕하세요","필통","전화기","마우스","충전기","TV", "지갑", "볼펜"]
rank={}
def sortV(x):
    return x[1]

    while True:
        print("1.문제불러오기 2.타자게임 3.등수목록4.저장하기5.불러오기")
        menu  = input("메뉴를 선택하세요\n")
    if menu=='1':
        f=open('basic/word.txt','r')
        line =1
        w.clear()
    while line:
        line = f.readline().replace("\n","")
        if not(line==''):
            w.append(line)
        print(w)
    elif menu=='2':
        menu=input("타자게임을 할려면 엔터를 누르세요\n")
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
        name = input("사용자 이름을 입력하세요")
        renk[name]=float(et)
    elif menu=='3':
        ranklist=sorted(rank.items(),key=sortV)
        um=1
        for k,v in ranklist:
            print("%d등 %s %f" %(num,k,v))
            num = num+1
    elif menu=='4':
        f=open('rank.txt','w')
        text=''
        items=rank.items()
        for k,v in items:
            text=text+k+':'+str(v)+'\n'
    f.writelines(text)
    f.close()
    elif menu=='5':
        f=open('rank.txt','r')
        line = 1
        while line:
            line = f.readline().replace("\n","")
            if not(line==''):
                k,v=line.split(':')
                rank[k]=float(v)
    else:
        

