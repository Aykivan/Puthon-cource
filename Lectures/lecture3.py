#  Функция - def
# Пример - функция которая суммирует все числа от 1 до n

# def sum_numbers(n, y = 'Hello'):
#     print(y) # Передали y значение по умолчанию Hello, если мы его сами не передает, то оно остается таким же
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
# #     print(summa) если убираем принт, то для вывода значения необходимо прописать return
#     return summa
#     print(stop) 
#     # return завершает работу функции, а значит все что написанно после него не работает

# a = sum_numbers(4)
# print(a)

#  Функция с неограниченным количеством аргументво
# def sum_str(*args): # С помощью * мы обозначаем неограниченное количество переменных
#     res = ''
#     for i in args:
#         res += i
#     return res

# a = sum_str('q', 'e', 'r', 'e', 'e')
# print(a)
# print(sum_str(1, 2, 3)) - не понятно

# Модульность - создание функций в отдельных файлах для повышения читабельности кода

# import modul3 # позволяет импортировать все функции данного модуля
# print(modul3.max1(5, 9))

# from modul3 import max1 # В данном случае мы импортируем только необходимую нам функцию
# # Мы можем вместо конкретной функции прописать * тогда мы импортируем все функции
# print(max1(5, 4)) # Обращение к функции в таком случае, будет выглядеть так

# import modul3 as m1 # Чтобы не писать длинное наименование модуля каждый раз, мы можем присвоить ему имя внутри основной программы
# print(m1.max1(5, 4))

# Рекурсия - функция, которая вызывает сама сибя

# : Последовательно Фибоначчи, это такая последовательность, в
# которой каждое последующее число равно сумму 2-ух предыдущих
# 💡 При описании рекурсии важно указать, когда функции надо
# остановиться и перестать вызывать саму себя. По-другому говоря, необходимо
# указать базис рекурсии

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n - 2) 
# Очень сложно не понятно, главное указать базис

# Алгоритмы
# Быстра сортировка 
# Быстрая сортировка принадлежит такой стратегии, как “разделяй и властвуй”.
# Сначала рассмотрим пример, затем напишем программный код
# Два друга решили поиграть в игру: один загадывает число от 1 до 100, другой
# должен отгадать. Согласитесь, что мы можем перебирать эти значения в случайном
# порядке, например: 32, 27, 60, 73… Да, мы можем угадать в какой-то момент, но что
# если мы обратиться к стратегии “разделяй и властвуй” Обозначим друзей, друг_1
# это Иван, который загадал число, друг_2 это Петр, который отгадывает. Итак
# начнем:

# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less =[i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)

# print(quick_sort([1, 4, 2, 3, 11, 36]))

# Сортировка слиянием

# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                     nums[k] = nums[left]
#                     i += 1
#             else:
#                 nums[k] = nums[right]
#                 j += 1 
#             k += 1 
#         while i < len[left]:
#             nums[k] = left[i]
#             i += 1
#             k += 1
#         while j < len[right]:
#             nums[k] = right[j]
#             i += 1
#             k += 1