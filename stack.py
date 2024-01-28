class Stack:
    def __init__(self):
        self.__list = []

    def push(self, __value):
        self.__list.append(__value)

    def pop(self):
        val = self.__list[-1]
        del self.__list[-1]
        return val

    def get_list(self):
        return self.__list
    def get_current(self):
        return self.__value


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def push(self, value):
        Stack.push(self, value)
        addStack = self.__sum
        addStack += value
        return addStack

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val


class Counter(AddingStack):
    def __init__(self):
        AddingStack.__init__(self)
        self.__counter = 0

    def get_counter(self, __value):
        AddingStack.push(self, __value)
        self.__counter += 1
        return self.__counter

    def pop(self):
        AddingStack.pop(self)
        self.__counter -= 1
        __counter = self.__counter
        return __counter


stack = Stack()
adding_stack = AddingStack()
counter = Counter()

from time import sleep
from random import randint

# print(counter.push(randint(0,10 ) for i in range(10))),
for me in range(randint(0, 10)):
    # sleep(0.5)
    print(counter.get_counter(randint(0, 10)))
    # print(counter.get_current())
    # print(counter.get_counter())
# print(counter.push(2))
print(counter.get_list())
print(counter.pop())
print(counter.get_list())

# print(counter.get_counter())
