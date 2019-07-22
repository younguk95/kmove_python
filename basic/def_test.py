'''def add(a,b):
    return a+b
    
print (add(5,4))
c=add(5,6)
print(c)

def add_many(choice, *a):
    result =0
    print(type(a))
    print(a)
    for i in a:
        result=result+i
    return result

total = add_many(1,2,3,4,5,6,7,8)
print(total)

def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a=1)
{'a':1}
print_kwargs(name='foo', age=3)
{'age':3 , 'name': 'foo'}

def add_and_mul(a,b):
    return a+b, a*b


add,mul = add_and_mul(3,6)
print(type(add))
print(type(mul))
print(add)
print(mul)



def say_myself(name,old,man=False):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("허영욱", 25)
say_myself("허영욱", 25 ,True)
'''

a=1
alist=[1,2,3]

def add_data():
    a=2
    alist.append(4)
    print("안 %d" %a)
add_data()
print("바깥쪽 %d" %a)
print(type(a))
print(type(alist))

print(alist)
