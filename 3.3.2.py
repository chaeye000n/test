year = int(input('년도를 입력하시오.'))
if (number % 4 == 0) and (number % 100 == 0) or (number % 400 == 0):
    print(year, '은(는) 윤년입니다.')
