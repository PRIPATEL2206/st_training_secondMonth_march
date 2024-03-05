from datetime import date
import datetime


cDate=date.today()
lastDate=date(cDate.year,cDate.month+1,1)-datetime.timedelta(1)
print(date(cDate.year,cDate.month,1))
print(lastDate)