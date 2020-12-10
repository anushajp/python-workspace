class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes:
            c_node = Node(data=nodes.pop(0))
            self.head = c_node
            for elem in nodes:
                c_node.next = Node(data=elem)
                c_node = c_node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append(None)
        return ' -> '.join([str(node) for node in nodes])

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if not self.head:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if not self.head:
            raise Exception('Linkedlist is empty')
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_befor(self, target_node_data, new_node):
        if not self.head:
            raise Exception('Linkedlist is empty')

        if target_node_data == self.head.data:

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception("Node with data '%s' not found" % target_node_data)



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


if __name__ == '__main__':
    llist = LinkedList()
    f_node = Node('a')
    s_node = Node('b')
    t_node = Node('c')
    fr_node = Node('d')
    f_node.next = s_node
    s_node.next = t_node
    t_node.next = fr_node
    llist.head = f_node
    print(llist)
    llist2 = LinkedList([1,2,3,4,5,6,7,8,9,0])
    print(llist2)
    llist2.add_first(Node(14))
    llist2.add_last(Node(7))
    llist2.add_after(14, Node(99))

    for item in llist2:
        print(item)
