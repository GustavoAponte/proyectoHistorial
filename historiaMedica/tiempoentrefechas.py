from datetime import date
from datetime import datetime
from dateutil import relativedelta

fecha_intr = input("Introduzca la fecha en formato dd-mm-aaaa: ")

dia_hoy = date.today()

fecha_inicial = datetime.strptime(fecha_intr, '%d-%m-%Y')

fecha_fin = dia_hoy.strftime('%d-%m-%Y')

fecha_fin = datetime.strptime(fecha_fin, '%d-%m-%Y')

tiempo_transc = relativedelta.relativedelta(fecha_fin, fecha_inicial)
print('Tiempo transcurrido: ',tiempo_transc.years,'años,',tiempo_transc.months,'meses,',tiempo_transc.days,'dias')
