from Node import Node

def astar(start, goal):
    print('astar')
    leftBank = start[0]
    rightBank = start[1]

    n = Node(0, leftBank, rightBank)
    n.expandChildren()
    n.printNode()
    n.printchildren()
    print()
    n.validate()
    n.printNode()
    n.printchildren()
    print()
