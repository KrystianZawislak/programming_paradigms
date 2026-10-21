begin, end=[int(input()) for _ in range(2)]

leap_years=[year for year in range(begin, end+1) if (year % 4 == 0 and year % 100) or year % 400 == 0]

print(leap_years)
