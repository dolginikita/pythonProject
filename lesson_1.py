#задание №1

durations = int(input('введите секунды: '))
days = durations // 86400
data_hours = durations % 86400
hour = data_hours // 3600
data_minutes = data_hours % 3600
minutes = data_minutes // 60
seconds = minutes % 60

print(days, "день", hour, "час", minutes, "минут", seconds, "секунд")


#задание№2

a = []
for i in range(1000):
    if i % 2 != 0:
        a.append(i ** 3)
print(a)

b = []
for num in b:
    sum1 = 0
    i = num
    while num != 0:
        sum1 += num % 10
        num = num // 10
    if sum1 % 7 == 0:
        b.append(i)
print(sum(b))

sum_num_plus = 0

for num in a:
    sum = 0
    i = num
    num += 17
    while num != 10:
        sum += num % 10
        num = num // 10
    if num % 7 == 0:
        sum_num_plus += i + 17

print(sum_num_plus)

#Задание №3

for n in range(1, 101):
    if (10 < n < 20) or (n % 10 in [0, 5, 6, 7, 8, 9]):
        print(n, "процентов")
    elif n % 10 == 1:
        print(n, "процент")
    else:
        print(n, "процента")