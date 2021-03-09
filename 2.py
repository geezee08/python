#Задача 2
ost = 10
sum_array = 0

array = [(x ** 2) for x in range(1, 1000, 2)]

for i in range(len(array)):
	sum_array_i = 0
	number = array[i]
	while number != 0:
		sum_array_i += number % ost
		number //= 10
	if sum_array_i % 7 == 0:
		sum_array += sum_array_i

print(sum_array)

for i in range(len(array)):
	array[i] += 17
	sum_array_i = 0
	number = array[i]
	while number != 0:
		sum_array_i += number % ost
		number //= 10
	if sum_array_i % 7 == 0:
		sum_array += sum_array_i

print(sum_array)