import datetime

dt_date = datetime.datetime.now()

print("The Current date is:", dt_date)

print("In specified format:", dt_date.strftime("%H:%M:%S"))
print(type(dt_date.strftime("%A, %d %b %Y")))
temps = dt_date.strftime("%H:%M:%S").rsplit(":", 2)
print(type(str(temps)))


temps1 = datetime.datetime.strptime("00:30:00","%H:%M:%S")
print(temps1)
