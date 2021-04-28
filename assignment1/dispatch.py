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
    n.validate()
    n.printNode()
    n.printchildren()
    print()
    for i in n.childNodes:
        i.expandChildren()
        i.validate()
        i.printNode()
        i.printchildren()
        for q in i.childNodes:
            q.expandChildren()
            q.validate()
            q.printNode()
            q.printchildren()
            for w in q.childNodes:
                w.expandChildren()
                w.validate()
                w.printNode()
                w.printchildren()
                for e in w.childNodes:
                    e.expandChildren()
                    e.validate()
                    e.printNode()
                    e.printchildren()
                    for r in e.childNodes:
                        r.expandChildren()
                        r.validate()
                        r.printNode()
                        r.printchildren()
                        for t in r.childNodes:
                            t.expandChildren()
                            t.validate()
                            t.printNode()
                            t.printchildren()
                            for y in t.childNodes:
                                y.expandChildren()
                                y.validate()
                                y.printNode()
                                y.printchildren()
                                for u in y.childNodes:
                                    u.expandChildren()
                                    u.validate()
                                    u.printNode()
                                    u.printchildren()
                                    for o in u.childNodes:
                                        o.expandChildren()
                                        o.validate()
                                        o.printNode()
                                        o.printchildren()
                                        print()
                                        for p in o.childNodes:
                                            p.expandChildren()
                                            p.validate()
                                            p.printNode()
                                            p.printchildren()

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
