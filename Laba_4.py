import random
from math import sqrt
mcheck = 0
mchange = 0

def merge_sorted(arrays):
    # берем массив отсортированных массивов и мерджим его в один
    global mcheck, mchange
    n = len(arrays) #размер массива
    indices = [0] * n # н нулей
    # в indices лежат индексы первого элемента, который мы еще не забрали
    result = [] #итоговый отсортированный массив
    while True:
        min_val = 1e100 # большой начальный минимум
        min_index = -1 # стартовый индекс
        for i in range(n):
            if indices[i] < len(arrays[i]): # если массив еще не закончился
                mcheck +=1 #счетчик проверок
                if arrays[i][indices[i]] < min_val: # если текущий элемент подмассива меньше нимимума
                    min_val = arrays[i][indices[i]] # меняем
                    min_index = i #запоминаем позицию
        if min_index == -1:
            break
            
        result.append(arrays[min_index][indices[min_index]]) # кладем минимум в результат
        mchange +=1
        indices[min_index] += 1 # переходим на следующий элемент в корзине
    return result #возврат отсортированного массива

def split_in_parts(a): #разбиваем исходный массив на подмассивы
    arrays = [] #массив массивов
    temp = [] #подмассив
    n = len(a) #длина массива
    m = int(sqrt(n)) # длина подмассива
    for i in a:
        temp.append(i) #увеличиваем подмассив
        if len(temp) >= m: #проверяем длину подмассива,если больше
            arrays.append(temp) #кладем подмассив темп в массив аррейс
            temp = [] #обнуляем подмассив
    if len(temp) > 0: #если мы прошли весь массив а, но подмассив остался не пустым
        arrays.append(temp) #дописываем то,что осталось в аррайс
    return arrays #возврат разбитого массива

flagg = False
while flagg == False: #считываем размер массива и проверяем
    print ('Размер массива: ')
    try:
        n = int(input())
        if n <= 0:
            print('Неверное число,введите еще раз!')
            flagg = False
        else:
            flagg = True
    except:
        print ('Введите повторно!')
        
flagg = False
while flagg == False: #считываем сам массив и проверяем
    try:
        print ('Введите элементы массива через ENTER: ')
        a = [int(input()) for i in range(n)]
        flagg = True
    except:
        print('Введите массив повторно!')
        p = False
#a = [random.randint(0,100) for i in range(500)]       
mfb = a #копирнули массив для пузырьковой сортировки

def sort_part(a):
    # сортировка пузырьком
    n = len(a)
    finished = False
    global mcheck, mchange
    while not finished:
        finished = True
        for i in range(n - 1):
            mcheck += 1 #проверки
            if a[i] > a[i + 1]:
                mchange += 1 #перестановки
                a[i], a[i + 1] = a[i + 1], a[i] # swap
                finished = False

b = split_in_parts(a) #кинули в б разбитый на куски а


for i in b: # циклично отсортировали каждую часть разбитого массива
    sort_part(i)

print('Исходный массив: ',a)
print('Блочный метод пузырьковой сортировки: ',merge_sorted(b))
print('Проверки: ',mcheck,'; Перестановки: ',mchange) #вывод исходного,отсортированного и проверки+перестановки

def bubble_sort (mfb): #отдельный пузырек для наглядности
    swap_test = False
    global bcheck, bchange
    bcheck = 0
    bchange = 0
    for i in range ( 0, len ( mfb ) - 1 ):
        for j in range ( 0, len ( mfb ) - i - 1 ):
            bcheck += 1
            if mfb[j] > mfb[j + 1]:
                mfb[j], mfb[j + 1] = mfb[j + 1], mfb[j]
                bchange += 1
                swap_test = True
        if swap_test == False:
            break

bubble_sort (mfb) #сортируем скопированный специально для этого массив
print('Пузырьковая сортировка: ',mfb)
print('Проверки: ',bcheck,'; Перестановки: ',bchange) #вывод
