class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList(object):
    def __init__(self):
        node = None
        self.__head = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def add(self, item):
        """头部添加"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def insert(self, pos, item):
        """任意位置插入"""
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            node = Node(item)
            cur = self.__head
            count = 0
            while count < (pos - 1):
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def append(self, item):
        """尾部添加"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def travel(self):
        cur = self.__head
        while cur is not None:
            print(cur.item, end=" ")
            cur = cur.next
        print("")


if __name__ == '__main__':
    link_list = SingleLinkList()
    link_list.append(2)
    link_list.append(3)
    link_list.insert(0, 1)
    link_list.insert(2, 4)
    link_list.insert(3, 5)
    link_list.travel()
