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


def is_valid(node: tuple, frontier: [tuple], explored: [tuple]) -> bool:
    if node[0] < 0 or node[1] < 0 or node[3] < 0 or node[4] < 0:
        return False
    elif (node[1] > node[0] != 0) or (node[4] > node[3] != 0):
        return False
    elif (node in frontier) or (node in explored):
        return False
    else:
        return True


def successor(node: tuple, frontier: [tuple], explored: [tuple]) -> [tuple]:
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
    prev = {}
    frontier = successor(start, (), ())
    explored = []
    n = 0

    for node in frontier:
        prev[node] = start

    while len(frontier):
        current = frontier.pop(0)
        if current == goal:
            return traceback(start, current, prev), n
        explored.append(current)
        n += 1
        for node in successor(current, frontier, explored):
            frontier.append(node)
            prev[node] = current

    return None, None


def dfs(start: tuple, goal: tuple) -> ([tuple], int):
    prev = {}
    frontier = successor(start, (), ())
    explored = []
    n = 0

    for node in frontier:
        prev[node] = start

    while len(frontier):
        current = frontier.pop()
        if current == goal:
            return traceback(start, current, prev), n
        explored.append(current)
        n += 1
        for node in successor(current, frontier, explored):
            frontier.append(node)
            prev[node] = current

    return None, None


def iddfs(start: tuple, goal: tuple) -> ([tuple], int):
    solution = None
    max_depth = 0
    while solution is None:
        n = 0
        prev = {}   # map node to prev node
        depth = {}  # map node to depth
        frontier = successor(start, (), ())
        explored = []

        depth[start] = 0
        for node in frontier:
            prev[node] = start
            depth[node] = 1

        while len(frontier):
            current = frontier.pop()
            if depth[current] > max_depth:
                continue
            if current == goal:
                return traceback(start, goal, prev), n
            explored.append(current)
            n += 1

            if depth[current] < max_depth:
                for node in successor(current, frontier, explored):
                    frontier.append(node)
                    prev[node] = current
                    depth[node] = depth[current] + 1

        max_depth += 1

    return None, None


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
    print("# of explored nodes = " + str(n))
    for i in range(len(solution)):
        print(str(i) + ": " + str(solution[i]))


def print_to_file(solution: [tuple], n: int, outfile: str):
    with open(outfile, 'w') as out:
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
