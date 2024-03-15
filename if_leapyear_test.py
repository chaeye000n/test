year = int(input('년도를 입력하시오.'))
is_leap_year = (number % 4 == 0) and (number % 400 == 0) or (number % 100 != 0)
print(year, '은(는) 윤년입니다.', is_leap_year)
