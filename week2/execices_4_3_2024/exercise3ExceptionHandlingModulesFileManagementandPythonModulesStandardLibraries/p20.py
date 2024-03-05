from datetime import date


myDOB=date(year=2002,month=11,day=30)

diff=(date.today()-myDOB).days
day=diff%30
month=((diff-day)//30)%12
year=(diff-day-30*month)//365

print(f"year : {year} , month : {month} ,  day : {day}")