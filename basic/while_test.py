listdata=[]
while True:
    print('''
    ==========리스트 데이터 관리======
    1.리스트에추가 2. 리스트 데이터 수정 3. 리스트 데이터 삭제 4. 종료
    ''')
    menu = int(input("메뉴를 선택하세요"))

    if menu == 4:
        break

    elif menu == 1:
        data=input("추가할 데이터를 입력하세요")
        listdata.append(data)
        print(listdata)
    elif menu == 2:
        data=input("추가할 데이터를 수정하세요")
        data=[len-1]
        data[2] = 4
        listdata.append(data)
        print(listdata)
    elif menu == 3:
        data=input("추가할 데이터를 삭제하세요")
        data=[len-1]
        del data[2]
        listdata.append(data)
        print(listdata)