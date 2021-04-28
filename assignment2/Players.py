'''
    Erich Kramer - April 2017
    Apache License
    If using this code please cite creator.

'''


class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    # PYTHON: use obj.symbol instead
    def get_symbol(self):
        return self.symbol

    # parent get_move should not be called
    def get_move(self, board):
        return minimax(board, self.symbol)


def minimax(board, symbol):
    children, moves = successor(board, symbol)
    results = []
    for child in children:
        if symbol == 'X':
            results.append(max_value(child, symbol))
        else:
            results.append(min_value(child, symbol))
        print(results)
        child.display()
    if symbol == 'X':
        index = results.index(max(results))
    else:
        index = results.index(min(results))
    return moves[index]


def max_value(board, symbol):
    if not board.has_legal_moves_remaining(symbol):
        return utility(board)
    else:
        v = float('-inf')
        children, moves = successor(board, symbol)
        for child in children:
            temp = min_value(child, 'O')
            if temp > v:
                v = temp
        return v


def min_value(board, symbol):
    if not board.has_legal_moves_remaining(symbol):
        return utility(board)
    else:
        v = float('inf')
        children, moves = successor(board, symbol)
        for child in children:
            temp = max_value(child, 'X')
            if temp < v:
                v = temp
        return v


def utility(board):
    p1 = 0
    p2 = 0
    for c in range(board.cols):
        for r in range(board.rows):
            if board.grid[c][r] == 'X':
                p1 += 1
            elif board.grid[c][r] == 'O':
                p2 += 1
            if c == 0 and r == 0:
                if board.grid[c][r] == 'X':
                    p1 += 10
                elif board.grid[c][r] == 'O':
                    p2 += 10
            if c == 0 and r == 3:
                if board.grid[c][r] == 'X':
                    p1 += 10
                elif board.grid[c][r] == 'O':
                    p2 += 10
            if c == 3 and r == 0:
                if board.grid[c][r] == 'X':
                    p1 += 10
                elif board.grid[c][r] == 'O':
                    p2 += 10
            if c == 3 and r == 3:
                if board.grid[c][r] == 'X':
                    p1 += 10
                elif board.grid[c][r] == 'O':
                    p2 += 10

    return p1 - p2


def successor(board, symbol):
    children = []
    moves = []
    for r in range(board.rows):
        for c in range(board.cols):
            if board.is_legal_move(c, r, symbol):
                child = board.cloneOBoard()
                child.play_move(c, r, symbol)
                moves.append([c, r])
                children.append(child)
    return children, moves


class HumanPlayer(Player):
    def __init__(self, symbol):
        Player.__init__(self, symbol);

    def clone(self):
        return HumanPlayer(self.symbol)

    # PYTHON: return tuple instead of change reference as in C++
    def get_move(self, board):
        col = int(input("Enter col:"))
        row = int(input("Enter row:"))
        return (col, row)


class MinimaxPlayer(Player):

    def __init__(self, symbol):
        Player.__init__(self, symbol);
        if symbol == 'X':
            self.oppSym = 'O'
        else:
            self.oppSym = 'X'
