import re
custlist=[]
page=-1

while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    ''').upper()

    if choice=="I": 
        customer={'name':'','sex':'',"email":'',"birthyear":''}       
        print("고객 정보 입력")
        customer['name']=input("이름")
        customer['sex']=input("성별")
        while True:
            customer['sex']=input("성별(M/m) 또는 F/f)을 입력하세요 : ").upper()
            if customer['sex'] in ('M','F'):
                break

        while True: #중복되지 않게 입력
            regex = re.compile('^[a-z][a-z0-9]{4,10}@[a-zA-Z]{2,6}[.][a-zA-Z]{2,3}$')
            while True:
                customer['email']=input("이메일을 입력하세요 : ")
                golbang = regex.search(customer['email'])
                print(golbang)
                if golbang:
                    break
                else:
                    print("@를 포함한 정확한 이메일을 써주세요")
            check=0
            for i in custlist:
                if i['email']==customer['email']:
                    check=1

            if check==0:
                break
            print('중복되는 이메일이 있습니다.')
        
        while True:
            customer['birthyear']=input("출생년도 4자리를 입력하세요 : ")

            if len(customer['birthyear'])== 4 and customer['birthyear'].isdigit():
                break

        print(customer)
        custlist.append(customer)
        print(custlist)
        page=len(custlist)-1
        print(page)
    
    elif choice=="C":
        if page >= 0:
            print("현재페이지 {}쪽 입니다.".format(page+1))
            print(custlist[page])
        else:
            print("입력된 정보가 없습니다.")
    
    elif choice == 'P':
        if page <=0:
            print("첫 번 째 페이지이므로 이전 페이지 이동이 불가능합니다. ")
            print(page)
        else:
            page -=1
            print("현재 페이지는 {}쪽 입니다.".format(page +1))
            print(custlist[page])
        
    elif choice == 'N':
        if page >= len(custlist)-1:
            print("마지막 페이지이므로 다음 페이지 이동이 불가합니다.")
            print([page])
        else:
            page +=1
            print("현재 페이지는 {}쪽입니다.".format(page+1))
            print(custlist[page])   
        
    elif choice=='D':
        choice = input('삭제하려는 고객 정보의 이메일을 입력하세요.')
        delok = 0
        for i in range(0,len(custlist)):
            if custlist[i]['email'] == choice:
                print('{} 고객님의 정보가 삭제되었습니다.'.format(custlist[i]['name']))
                del custlist[i]
                print(custlist)
                delok = 1
                break
        if delok == 0:
            print('등록되지 않은 이메일입니다.')
            print(custlist)
       
    elif choice=="U":
        choice1 = input('수정하려는 고객 정보의 이메일을 입력하세요.')
        idex=-1
        for i in range(0,len(custlist)):
            if custlist[i]['email'] == choice1:
                idx=i
                break
        if idx ==-1:
            print("등록되지 않은 이메일입니다.")
            break
        choice2=input('''
        다음중 수정하실 정보를 골라주세요
        name sex birthyear
        (수정할 정보가 없으며 'exit' 입력)
        ''')


        if choice2 in ('name','sex', 'birthyear'):
            custlist[idx][choice2]=input('수정할{}을 입력하세요 : '.format(choice2))
            break
        elif choice2 == 'exit':
            break
        else:
            print("존재하지 않는 정보입니다.")
            break

        print("고객 정보 수정")
    elif choice=="Q":
        print("프로그램 종료")
        break
    else:
        print("잘못입력하셨습니다.")
