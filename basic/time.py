import time

input(" 시작할때 엔터를 누르세요")
t1 = time.time()
input("20 초 후에 다시 엔터를 누릅니다")
t2 = time.time()
et = t2-t1
print("실제시간", et, "초")
print("차이" , abs(et - 20),"초")