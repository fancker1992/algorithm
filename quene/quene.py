class Quene(object):
    def __init__(self):
        self.__item = []

    def push(self, item):
        self.__item.insert(0, item)

    def pop(self):
        return self.__item.pop()

    def is_empty(self):
        return self.__item == []

    def size(self):
        return len(self.__item)


if __name__ == '__main__':
    quene = Quene()
    quene.push(4)
    quene.push(1)
    quene.push(2)
    quene.push(3)
    for i in range(quene.size()):
        print(quene.pop())
