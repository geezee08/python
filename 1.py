#Задача 1
duration = int(input('Введите время в секундах: '))
if duration < 60: #до минуты
	print(duration, 'сек')
elif duration < (60 * 60): #до часа
	print(f'{duration // 60} мин, {duration % 60} сек')
elif duration < (60 * 60 * 24): #до суток
	print(f'{duration // (60 * 60)} час, {(duration // 60 % 60)} мин, {duration % 60} сек')
