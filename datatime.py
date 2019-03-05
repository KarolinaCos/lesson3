from datetime import date, timedelta, datetime
day_now = date.today()
print("Today is", day_now)
delta = timedelta(days=1)
day_yesterday = day_now - delta
print("Yesterday was:", day_yesterday)

#delta2 = timedelta(month=1)
one_month_ago = day_now.replace(month=day_now.month - 1, day = 1)
print("One month ago was", one_month_ago)

date_string = "01/01/17 12:10:03.234567"
date_dt = datetime.strptime(date_string, "%d/%m/%y %I:%M:%S.%f") 
print(date_dt)


