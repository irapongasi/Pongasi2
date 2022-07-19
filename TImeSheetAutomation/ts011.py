import datetime


date_str = 'Mar 7 - 12, 2022' #sample range


splitrange = date_str.split('-')
mdate = splitrange[0].split(' ')

yr_split = splitrange[1].split(",")

yr = int(yr_split[1])
current_month = mdate[0]
start_date = int((mdate[1]))
days_covered = int((mdate[1])) + 7
if days_covered > 30:
    days_covered -= 30


my_date = datetime.date.today()

a = str(my_date.strftime("%b"))
b = int(my_date.strftime("%d"))
c = int(my_date.strftime('%Y'))


if (start_date + 7) >= 28:
    start_date = 0

if current_month == a and yr == c:
    if start_date <= b <= days_covered:
        print("Displayed week is the current week")
else:
    print("Displayed week is not the current week")










#range = str(((int(my_date.day)) + 7))
#y = str(my_date.strftime("%Y"))
#c = a + " " + b + " - " + range + ", " + y
#print(c)


