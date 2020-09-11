<<<<<<< HEAD
<<<<<<< HEAD
import sys

def swap(arr, idx1, idx2):
    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

# Просеивание вверх i-го элемента массива
def sift_up(arr, i):
    key = 0
    #i = len(arr) - 1
    # Просеивание вверх
    while (i > 0) and (arr[i][key] < arr[(i - 1) // 2][key]):
        swap(arr, i, (i - 1) // 2)
        i = (i - 1) // 2

# Просеивание вниз первого элемента массива
def sift_down(arr):
    key = 0
    i = 0
    while (2 * i + 1) < len(arr):
        # Назначим левого ребенка минимумом
        min_idx = 2 * i + 1
        # Если есть правый ребенок и он меньше левого, то он - минимум
        if (2 * i + 2) < len(arr):
            if arr[2 * i + 2][key] < arr[2 * i + 1][key]:
                min_idx = 2 * i + 2
        # Если наименьший из детей меньше текщего элемента, меняем местами
        if arr[min_idx][key] < arr[i][key]:
            swap(arr, i, min_idx)
        # В противном случае дерево сбалансировано, прерываем цикл
        else:
            break
        i = min_idx

# Поиск индекса нужного элемента массива по номеру операции
# Куча представляет собой список, в каждой ячейке которого хранится 
# по индексу 0 - значение, по индексу 1 - номер операции
def find(arr, operation_id):
    key = 1
    result = -1
    for i in range(len(arr)):
        if arr[i][key] == operation_id:
            result = i
            break
    return result

arr = []
i = 0

for line in sys.stdin:
    #print(line, end = '')
    i += 1
    command = line.split()
    if command[0] == 'push':
        arr.append([int(command[1]), i])
        sift_up(arr, len(arr) - 1)
    elif command[0] == 'decrease-key':
        # Найдем индекс элемента массива с нужным номером операции
        idx = find(arr, int(command[1])) 
        if idx >= 0:
            arr[idx][0] = int(command[2])
            sift_up(arr, idx)
    else: # extract-min
        if len(arr) > 0:
            result = arr[0]  # сохраняем минимум
            swap(arr, 0, -1) # меняем местами первый с последним элементом
            del arr[-1] # удаляем последний элемент
            sift_down(arr)
            print(result[0], result[1])
        else: # очередь пуста
            print('*')
=======
def f(x):
    x.append((1,3))
=======
import sys
>>>>>>> fb57725... Add algorithms solutions WEEK5

def swap(arr, idx1, idx2):
    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

# Просеивание вверх i-го элемента массива
def sift_up(arr, i):
    key = 0
    #i = len(arr) - 1
    # Просеивание вверх
    while (i > 0) and (arr[i][key] < arr[(i - 1) // 2][key]):
        swap(arr, i, (i - 1) // 2)
        i = (i - 1) // 2

<<<<<<< HEAD
print(a)
>>>>>>> 556a71b... fetch linal from repo
=======
# Просеивание вниз первого элемента массива
def sift_down(arr):
    key = 0
    i = 0
    while (2 * i + 1) < len(arr):
        # Назначим левого ребенка минимумом
        min_idx = 2 * i + 1
        # Если есть правый ребенок и он меньше левого, то он - минимум
        if (2 * i + 2) < len(arr):
            if arr[2 * i + 2][key] < arr[2 * i + 1][key]:
                min_idx = 2 * i + 2
        # Если наименьший из детей меньше текщего элемента, меняем местами
        if arr[min_idx][key] < arr[i][key]:
            swap(arr, i, min_idx)
        # В противном случае дерево сбалансировано, прерываем цикл
        else:
            break
        i = min_idx

# Поиск индекса нужного элемента массива по номеру операции
# Куча представляет собой список, в каждой ячейке которого хранится 
# по индексу 0 - значение, по индексу 1 - номер операции
def find(arr, operation_id):
    key = 1
    result = -1
    for i in range(len(arr)):
        if arr[i][key] == operation_id:
            result = i
            break
    return result

arr = []
i = 0

for line in sys.stdin:
    #print(line, end = '')
    i += 1
    command = line.split()
    if command[0] == 'push':
        arr.append([int(command[1]), i])
        sift_up(arr, len(arr) - 1)
    elif command[0] == 'decrease-key':
        # Найдем индекс элемента массива с нужным номером операции
        idx = find(arr, int(command[1])) 
        if idx >= 0:
            arr[idx][0] = int(command[2])
            sift_up(arr, idx)
    else: # extract-min
        if len(arr) > 0:
            result = arr[0]  # сохраняем минимум
            swap(arr, 0, -1) # меняем местами первый с последним элементом
            del arr[-1] # удаляем последний элемент
            sift_down(arr)
            print(result[0], result[1])
        else: # очередь пуста
            print('*')
>>>>>>> fb57725... Add algorithms solutions WEEK5
