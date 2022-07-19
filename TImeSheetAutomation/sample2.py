import datetime as dt


mytime = dt.datetime.strptime('073000', '%H%M%S').time()
print(mytime)
print(dt.date.today())
mydatetime = dt.datetime.combine(dt.date.today(), mytime)
print(mydatetime)