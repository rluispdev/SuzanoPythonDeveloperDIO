import datetime

d = datetime.datetime.now()

#formatando data e hora
print(d.strftime("%d/%m/%Y %H:%M:%S"))

#Convertendo string para datatime
date_string = "01/01/2021 12:10:03"
d = datetime.datetime.strptime(date_string, "%d/%m/%Y %H:%M:%S")
print(d)

 

