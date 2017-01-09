class Node:
    def __init__(self, value, children=[]):
        self.children = children
        self.value = value

    def tree_level_order(self):
        level = [self]
        while level:
            print(''.join([str(node.value) for node in level]))
            level = [children for node in level for children in node.children]

    def tree_lvo(self):
        level = [self]
        ret = ''
        while level:
            ret += ''.join([str(node.value) for node in level]) + '\n'
            t = []
            for node in level:
                for children in node.children:
                    t.append(children)
            level = t
        print(ret)

tree = Node(1,
            [Node(2, [Node(4)]),
             Node(3, [Node(5),
                      Node(6)])])

tree

tree.tree_level_order()

tree.tree_lvo()
