import datetime

#criando datetime
d = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3),"BRT"))
print(d)

#convertendo para outro timezone
d_utc = d.astimezone(datetime.timezone.utc)
print(d_utc)