import re,pickle,os
custlist=[]
page = -1

def exe(choice):
        if choice=='I':
            insertData()
        
        elif choice=='C':
            curSearch()
        
        elif choice=='P':
            preSearch()

        elif choice=='N':
            nextSearch()

        elif choice=='U':
            updateData()
        
        elif choice=='D':
            deleteData()
        
        elif choice=='Q':
            saveData()
            quit()

def insertData():        
    customer={'name':'','sex':'',"email":'',"birthyear":''}
    customer['name']=str(input("이름을 입력하세요 : "))
        
    while True:
            customer['sex']=str(input("성별(M/m 또는 F/f)을 입력하세요 : "))
            customer['sex']=customer['sex'].upper()
            if customer['sex'] in ('M','F'):
                break
            else:
                print('M/m 또는 F/f 중 입력해주세요')

    while True: # 중복되지 않게 입력
        regex = re.compile('^[a-z][a-z0-9]{4,10}@[a-zA-Z]{2,6}[.][a-zA-Z]{2,3}$')
        while True:
            customer['email']=input("이메일을 입력하세요 : ") 
            golbang = regex.search(customer['email'])
            if golbang:
                break
            else:
                print('"@"를 포함한 정확한 이메일을 써주세요')

        check=0
        for i in custlist:
            if i['email']==customer['email']:
                check=1
        
        if check==0:
            break
        print('중복되는 이메일이 있습니다.')    
            

    while True:
        customer['birthyear']=input("출생년도 4자리를 입력해주세요 : ")
        
        if len(customer['birthyear']) == 4 and customer['birthyear'].isdigit():
            break

    print(customer)
    custlist.append(customer)
    print(custlist)
    global page
    #page += 1
    page=len(custlist)-1   
    print(page)  
    
def curSearch():
    global page
    if page >= 0:
        print("현재 페이지는 {}쪽 입니다".format(page + 1)) 
        print(custlist[page])
    else:
        print("입력된 정보가 없습니다.")    

def preSearch():
    global page
    if page <= 0:
        print('첫 번 째 페이지이므로 이전 페이지 이동이 불가합니다')
        print(page)
    else:
        page -= 1
        print("현재 페이지는 {}쪽 입니다".format(page + 1))
        print(custlist[page])
        
def nextSearch():
    global page
    if page >= len(custlist)-1:
        print('마지막 페이지이므로 다음 페이지 이동이 불가합니다')
        print(page)
    else:
        page += 1
        print("현재 페이지는 {}쪽 입니다".format(page + 1))
        print(custlist[page])

def deleteData():
    global page
    choice1 = input('삭제하려는 고객 정보의 이메일을 입력하세요.')
    delok = 0
    for i in range(0,len(custlist)):
        if custlist[i]['email'] == choice1:
            print('{} 고객님의 정보가 삭제되었습니다.'.format(custlist[i]['name']))
            del custlist[i]
            print(custlist)
            page=len(custlist)-1   
            print(page)  
            delok = 1            
            break

    if delok == 0:
            print('등록되지 않은 이메일입니다.')

def updateData(): 
    while True:
        choice1=input('수정하시려는 고객 정보의 이메일을 입력하세요 : ')
        idx=-1
        for i in range(0,len(custlist)):
            if custlist[i]['email'] == choice1:
                idx=i
                break
        if idx==-1:
            print('등록되지 않은 이메일입니다.')       
            break
                    
        choice2=input('''
        다음 중 수정하실 정보를 골라주세요 
                name, sex, birthyear
        (수정할 정보가 없으면 'exit' 입력)
        ''')
        if choice2 in ('name','sex','birthyear'):
            custlist[idx][choice2]=input('수정할 {}을 입력하세요 :'.format(choice2))
            break
        elif choice2 =='exit':
            break
        else:
            print('존재하지 않는 정보입니다.')
            break
 
def saveData():
    with open('basic/data.pkl','wb') as f:
        pickle.dump(custlist,f)
       
def loadData():
    #파일 크기가 0보다 클 경우에  읽어옴.
    #if os.path.getsize('basic/data.pkl')>0: 
    #파일이 존재할 경우에 읽어옴.
    global page,custlist
    if os.path.exists('basic/data.pkl'):    
        with open('basic/data.pkl','rb') as f:
            custlist=pickle.load(f)
            page=len(custlist)-1