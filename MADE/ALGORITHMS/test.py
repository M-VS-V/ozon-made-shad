<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> fb57725... Add algorithms solutions WEEK5
import sys


class Node:
    def __init__(self, data, operation):
        self.data = int(data)
        self.operation = operation


class Heap:
    def __init__(self):
        self.list = []
        self.push = 0

    def prn(self):
        str_arr = ''
        for i in self.list:
            str_arr += str(i.data) + ' '
        sys.stdout.write(str_arr + '\n')

    def insert(self, data):
        element = Node(data, self.push)
        self.list.append(element)
        self.norm_heap_up(len(self.list) - 1)

    def norm_heap_down(self):
        i = 0
        while (2 * i + 1) < len(self.list):
            left = 2 * i + 1
            right = 2 * i + 2
            j = left
            if right < len(self.list) and self.list[right].data < self.list[left].data:
                j = right
            if self.list[i].data <= self.list[j].data:
                break
            self.swap(i, j)
            i = j

    def swap(self, i, j):
          self.list[i], self.list[j] = self.list[j], self.list[i]

    def norm_heap_up(self, cur):
        i = cur
        while self.list[i].data < self.list[(i - 1) // 2].data and i > 0:
            self.swap(i, (i - 1) // 2)
            i = (i - 1) // 2

    def remove_min(self):
        if len(self.list) < 1:
            return '*'
        else:
            deleted = self.list[0]
            self.list[0] = self.list[-1]
            self.list.pop()
            self.norm_heap_down()
            return deleted

    def decrease(self, operation, value):
        operation = int(operation)
        value = int(value)
        for i in range(len(self.list)):
            if self.list[i].operation == operation:
                self.list[i].data = value
                self.norm_heap_up(i)
                return


answer = Heap()
for line in sys.stdin:
    question = line.split()
    answer.push += 1
    if question[0] == 'push':
        answer.insert(question[1])
    elif question[0] == 'extract-min':
        output = answer.remove_min()
        if output == '*':
            sys.stdout.write('*\n')
        else:
            print(f'{output.data} {output.operation}')
    elif question[0] == 'decrease-key':
        answer.decrease(question[1], question[2])
<<<<<<< HEAD
=======
import inspect, traceback
a = 1_000_000
b = 1_000_000
print(a is b)
print(id(a))
print(id(b))

def foo():
    a1 = 1_000_000
    b1 = 1_000_000
    print(a1 is b1)
    print(id(a1))
    print(id(b1))

foo()
print(inspect.stack())
>>>>>>> 556a71b... fetch linal from repo
=======
>>>>>>> fb57725... Add algorithms solutions WEEK5
