import sys

class Stack:
    def __init__(self):
        self.head = None


    def isEmpty(self):
        return self.head is None


    def append(self, value):
        self.head = Stack.Node(self.head, value)


    def peek(self):
        return self.head.value


    def pop(self):
        self.head = self.head.next


    class Node:
        def __init__(self, next, value):
            self.value = value
            self.next = next
    

class ProblemSolver:
    def solve(self):
        stack = Stack()
        _ = int(input())
        
        for line in sys.stdin:
            commands = list(map(int, line.split()))

            if commands[0] == 1:
                val = commands[1]
                
                if stack.isEmpty():
                    stack.append((val, val))
                else:
                    stack.append((val, min(stack.peek()[1], val)))
            elif commands[0] == 2:
                stack.pop()
            else:
                print(stack.peek()[1])


ProblemSolver().solve()