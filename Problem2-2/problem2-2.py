from datetime import datetime
todays_date = datetime.now()
birth_date = input()
birth_year = int(birth_date.split("/")[0])
birth_month = int(birth_date.split("/")[1])
birth_day = int(birth_date.split("/")[2])
if (birth_month > 12):
    print("WRONG")
elif (birth_day > 31):
    print("WRONG")
else:
    birth_date = datetime(birth_year, birth_month, birth_day)
    age = todays_date - birth_date
    age = age.days // 365
    print(age)