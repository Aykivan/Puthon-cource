# a = 'hello'
# for i in a:
# print(i, end='')

# for e in range(10, 2, -2):
# print(e)

# for ind in range(0, len(a)): # 0, 1, 2, 3, 4
# print(a[ind])


# for _ in range(3): # 0, 1, 2
# print('HELLO'

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# 9. По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while

# n = int(input())
# i = 1
# factorial = 1
# if n > 0:
#     while i <= n:
#         factorial *= i
#         i += 1
#     print(factorial)
# else:
#     print(1)

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# 11. Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1

# n = int(input('Введите число: '))
# fib1 = int(0)
# fib2 = int(1)
# count = 3

# while fib1 + fib2 <= n:
#     fib1 = fib2
#     fib2 = fib_sum
#     fib_sum = fib1 + fib2
#     count += 1
# if n == fib_sum:
#     print('YES', count)
# else:
#     print('NO')

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# 13. Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений за погодой. 
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. 
# Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 
# градусов Цельсия. Напишите программу, помогающую синоптикам в работе.

# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50

# n = int(input('Введите количество дней (от 1 до 100): '))
# max_count = 0
# count = 0 
# for _ in range(n):
#     temp = int(input(f"Введите температуру: "))
#     if temp >= 0:
#         count += 1
#     else: 
#         if count > max_count:
#             max_count = count
#         count = 0
# if max_count == 0 and count != 0:
#     print(count)
# else:
#     print(max_count)

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# 15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, 
# а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое. Здесь каждое число – это масса 
# соответствующего арбуза. Все числа натуральные и не превышают 30000.

# n = int(input('Введите количество арбузов: '))
# max_ar = 0
# min_ar = 30000 
# for _ in range(n):
#     ves = int(input(f"Введите вес: "))
#     if ves > max_ar:
#         max_ar = ves
#     else: 
#         if ves < min_ar:
#             min_ar = ves
# print(f'Вес арбуза для себя - {max_ar}, вес арбуза для тещи - {min_ar}')
 


