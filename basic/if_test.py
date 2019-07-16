jumsu = int(input("성적을 입력하세요"))
print('입력한 성적은 %s입니다.' %jumsu)

if jumsu >= 90:
    total = 'A'
elif  jumsu >= 80:
    total = 'B'
elif jumsu >= 70:
    total = 'C'
elif jumsu >= 60:
    total = 'D'
else:
    total = 'F'
print('당신의 학점은 {}입니다.' .format(total))

