class Stack(object):
    """栈"""

    def __init__(self):
        self.__item = []

    def push(self, item):
        """添加一个新的元素到栈顶"""
        self.__item.append(item)

    def pop(self):
        """从栈顶弹出一个元素"""
        return self.__item.pop()

    def is_empty(self):
        return self.__item == []

    def peek(self):
        """返回栈顶元素"""
        return self.__item[-1]

    def size(self):
        return len(self.__item)


if __name__ == '__main__':
    stack = Stack()
    stack.push(123)
    print(stack.peek())
    print(stack.size())
    print(stack.is_empty())
