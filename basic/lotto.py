import random ##외장함수
for i in range(5):
    lotto = [0,0,0,0,0,0]
    for x in range(6):
        num=0
        while(num in lotto):
            num=random.randint(1,45)
        lotto[x]=num
    print("로또 : " ,sorted(lotto))

import random
for i in range(1,6):
    print("로또 : ", sorted(random.sample(range(1,46),6)))