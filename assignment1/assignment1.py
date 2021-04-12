from copy import copy
import sys
import csv


expansions = {
    0: (1, 0),
    1: (2, 0),
    2: (0, 1),
    3: (1, 1),
    4: (0, 2)
}

cutoff = (-1, -1, -1, -1, -1, -1)
max_depth = 1000


def is_valid(node: tuple, frontier: [tuple], explored: [tuple]) -> bool:
    if node[0] < 0 or node[1] < 0 or node[3] < 0 or node[4] < 0:
        return False
    elif (node[1] > node[0] != 0) or (node[4] > node[3] != 0):
        return False
    elif (node in frontier) or (node in explored):
        return False
    else:
        return True


def expand(node: tuple, explored: [tuple], frontier: [tuple]) -> [tuple]:
    successors = []
    for i in range(5):
        node_cpy = list(copy(node))
        if node_cpy[2] == 1:  # boat is on left bank
            node_cpy[0] -= expansions[i][0]
            node_cpy[3] += expansions[i][0]
            node_cpy[1] -= expansions[i][1]
            node_cpy[4] += expansions[i][1]
            node_cpy[2] = 0
            node_cpy[5] = 1
            node_cpy = tuple(node_cpy)
        else:  # boat is on right bank
            node_cpy[0] += expansions[i][0]
            node_cpy[3] -= expansions[i][0]
            node_cpy[1] += expansions[i][1]
            node_cpy[4] -= expansions[i][1]
            node_cpy[2] = 1
            node_cpy[5] = 0
            node_cpy = tuple(node_cpy)
        if is_valid(node_cpy, frontier, explored):
            successors.append(node_cpy)
    return successors


def traceback(start: tuple, stop: tuple, prev: dict) -> [tuple]:
    solution = []
    tmp = stop
    while tmp != start:
        solution.append(tmp)
        tmp = prev[tmp]
    solution.append(start)
    solution.reverse()
    return solution


def bfs(start: tuple, goal: tuple) -> ([tuple], int):
    if start == goal:
        return [start], 0
    explored = []
    frontier = [start]
    prev = {}
    while len(frontier):
        node = frontier.pop(0)
        explored.append(node)
        for successor in expand(node, explored, frontier):
            prev[successor] = node
            if successor == goal:
                return traceback(start, successor, prev), len(explored)
            frontier.append(successor)
    return None, None


def dls(start: tuple, goal: tuple, limit: int) -> ([tuple], int):
    cutoff_reached = False
    explored = []
    frontier = [start]
    prev = {}
    depth = {start: 0}
    while len(frontier):
        node = frontier.pop()
        if depth[node] >= limit:
            cutoff_reached = True
            continue
        explored.append(node)
        for successor in expand(node, explored, frontier):
            prev[successor] = node
            depth[successor] = depth[node] + 1
            if successor == goal:
                return traceback(start, successor, prev), len(explored)
            frontier.append(successor)
    if cutoff_reached:
        return cutoff, None
    else:
        return None, None


def dfs(start: tuple, goal: tuple) -> ([tuple], int):
    return dls(start, goal, max_depth)


def iddfs(start: tuple, goal: tuple) -> ([tuple], int):
    if start == goal:
        return [start], 0
    limit = 0
    while limit in range(max_depth):
        solution, n = dls(start, goal, limit)
        if solution == cutoff:
            limit += 1
            continue
        elif solution == None:
            return None, None
        else:
            return solution, n
    return cutoff, None


def astar(start, goal) -> ([tuple], int):
    raise NotImplementedError


def parse(filename: str) -> tuple:
    with open(filename, 'r') as fd:
        reader = csv.reader(fd)
        data = next(reader)
        data += next(reader)
        for i in range(len(data)):
            data[i] = int(data[i])
        return (data[0], data[1], data[2], data[3], data[4], data[5])


def print_to_screen(solution: [tuple], n: int):
    if solution is None:
        print("No solution found")
    elif solution == cutoff:
        print("search reached cutoff")
    else:
        print("# of explored nodes = " + str(n))
        for i in range(len(solution)):
            print(str(i) + ": " + str(solution[i]))


def print_to_file(solution: [tuple], n: int, outfile: str):
    with open(outfile, 'w') as out:
        if solution is None:
            print("No solution found", file=out)
        else:
            print("# of explored nodes = " + str(n), file=out)
            for i in range(len(solution)):
                print(str(i) + ": " + str(solution[i]), file=out)


if __name__ == '__main__':
    if len(sys.argv) < 5:
        print("incorrect number of arguments: " + str(len(sys.argv)))
        exit(1)

    start = parse(sys.argv[1])
    goal = parse(sys.argv[2])

    solution = []
    n = 0

    mode = sys.argv[3]
    if mode == "bfs":
        solution, n = bfs(start, goal)
    elif mode == "dfs":
        solution, n = dfs(start, goal)
    elif mode == "iddfs":
        solution, n = iddfs(start, goal)
    elif mode == "astar":
        solution, n = astar(start, goal)
    else:
        print("incorrect mode: \"" + mode + "\"")

    print_to_screen(solution, n)
    print_to_file(solution, n, sys.argv[4])
