from searchMethods.astar import astar
from searchMethods.bfs import bfs
from searchMethods.dfs import dfs
from searchMethods.iddfs import iddfs

def dispatch(start, goal, mode, outFile):
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
