from datetime import datetime

def get_1000_year(start_year):
    year_day_1000 = 0 

    for year in range(start_year, start_year+1000):
        if year % 400 == 0:
            year_day_1000 += 366
        elif year % 100 == 0:
            year_day_1000 += 365
        elif year % 4 == 0 :
            year_day_1000 += 366
        else:
            year_day_1000 += 365
    
    return year_day_1000


def d_day(today, dday):
    # year, month, date를 정해서 총 datetime 구하기 
    today_date = datetime(year = today[0], month = today[1], day = today[2])
    dday_date = datetime(year = dday[0], month = dday[1], day = dday[2])

    # datetime의 days 값을 저장 
    # datetime 간의 차를 구하면 days, 시분초의 정보가 나옴
    dday_day = (dday_date - today_date).days

    year_day_1000 = get_1000_year(start_year = today[0]) # 1000년을 넘는지 안넘는지 확인 

    if dday_day >= year_day_1000:
        print("gg")
    else:
        print(f"D-{dday_day}")

today = list(map(int,input().split()))
dday = list(map(int,input().split()))

d_day(today, dday)