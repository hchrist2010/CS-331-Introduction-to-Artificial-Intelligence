from searchMethods.astar import astar
from searchMethods.bfs import bfs
from searchMethods.dfs import dfs
from searchMethods.iddfs import iddfs
from Node import Node


def dispatch(start, goal, mode, outFile):
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
    if(mode == 'astar'):
        astar(start, goal)
    elif(mode == 'bfs'):
        bfs(start, goal)
    elif(mode == 'dfs'):
        dfs(start, goal)
    elif(mode == 'iddfs'):
        idffs(start, goal)
    else:
        print('Mode not defined')
