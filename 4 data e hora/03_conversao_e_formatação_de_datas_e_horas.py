import datetime

d = datetime.datetime.now()

#formatação de data e hora
print( d.strftime("%d/%m/%Y %H:%M"))

#Convertendo string para datetime

date_string = "25/03/2025 18:55"
d = datetime.datetime.strptime(date_string, "%d/%m/%Y %H:%M")
print(d)