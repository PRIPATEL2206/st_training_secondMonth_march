from datetime import date
import datetime

cDate=date.today()
cDate=date(cDate.year,cDate.month,1)
while cDate.weekday()!= 0:
    cDate=cDate+datetime.timedelta(1)
for i in  range(7):
    print(cDate)
    cDate=cDate+datetime.timedelta(1)


