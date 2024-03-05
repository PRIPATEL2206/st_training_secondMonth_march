import datetime 


def formateDate(da:datetime.datetime):
    return da.strftime("%dth %B %Y %A %I:%M:%S %p")

cDate=datetime.datetime.now()
lastDate=datetime.datetime(cDate.year,cDate.month+1,1)-datetime.timedelta(1)
print(formateDate(datetime.datetime(cDate.year,cDate.month,1)))
print(formateDate(lastDate))