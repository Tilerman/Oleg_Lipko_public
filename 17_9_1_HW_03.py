# Напишите программу, которой на вход подается последовательность чисел через пробел,
# а также запрашивается у пользователя любое число.
# В качестве задания повышенного уровня сложности можете выполнить проверку соответствия указанному
# в условии ввода данных.
# Далее программа работает по следующему алгоритму:
# -Преобразование введённой последовательности в список
# -Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)
# -Устанавливается номер позиции элемента, который меньше введенного пользователем числа,
# а следующий за ним больше или равен этому числу.
# При установке позиции элемента воспользуйтесь алгоритмом двоичного поиска, который был рассмотрен в этом модуле. Реализуйте его также отдельной функцией.
# Подсказка
#
# Помните, что у вас есть числа, которые могут не соответствовать заданному условию.
# В этом случае необходимо вывести соответствующее сообщение
str = ''
str1 = ''
element = 0
# print(len(array))
while(len(str) <= 8):
    str = input("Введите через пробел пять целых чисел от 1 до 10 :")
L = str.split() #преобразуем в список
try:
    for x in L:
        int(x)
except ValueError: #исключаем ошибку int(x), когда x символ, а не цифра
    print("Введены неверные символы")
else:
    array = list(map(int, str.split()))
finally:
    print(array)
while(not str1.isnumeric()):
    str1 = input("Введите любую цифру :")
if len(str1) > 1:
    print("Введена неверная цифра")
else:
    element = int(str1)

def sort_incr(array): # функция сортировки пузырьком
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array

array = sort_incr(array)
print(array)

def binary_search(array, element, left, right): #функция бинарного поиска
    if left > right: # если левая граница превысила правую,
        return False # значит элемент отсутствует

    middle = (right+left) // 2 # находимо середину
    if array[middle] == element: # если элемент в середине,
        return middle # возвращаем этот индекс
    elif element < array[middle]: # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle-1)
    else: # иначе в правой
        return binary_search(array, element, middle+1, right)

left = 0
right = len(array) -1
if not binary_search(array, element, left, right):
    print("Число находится вне диапазона последовательности")
else:
    print("Указатель на предыдущее число последовательности равен: ", binary_search(array, element, left, right) -1)
