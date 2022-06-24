import datetime

#now = datetime.datetime.now() + datetime.timedelta(days=7)
#due = now.strftime("%y-%m-%d")
#print(due)


temp = datetime.datetime.now()
now = temp.strftime("%y-%m-%d")
due = temp + datetime.timedelta(days=7)
due_date = due.strftime("%y-%m-%d")

print(due_date)