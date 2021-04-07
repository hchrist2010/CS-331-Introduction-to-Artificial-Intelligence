class Node:
    def __init__(self, parent, leftBank, rightBank):
        self.parent = parent
        self.leftBank = leftBank
        self.rightBank = rightBank
        self.childNodes = []

    def expandChildren(self):
        if(self.leftBank[2] == 1):
            if(self.leftBank[0] >= 1):
                left = self.leftBank.copy()
                left[0] = left[0] - 1
                left[2] = 0
                right = self.rightBank.copy()
                right[0] = right[0] + 1
                right[2] = 1
                temp = Node(self, left, right)
                self.childNodes.append(temp)
            if(self.leftBank[0] >= 2):
                left = self.leftBank.copy()
                left[0] = left[0] - 2
                left[2] = 0
                right = self.rightBank.copy()
                right[0] = right[0] + 2
                right[2] = 1
                temp = Node(self, left, right)
                self.childNodes.append(temp)
            if(self.leftBank[1] >= 1):
                left = self.leftBank.copy()
                left[1] = left[1] - 1
                left[2] = 0
                right = self.rightBank.copy()
                right[1] = right[1] + 1
                right[2] = 1
                temp = Node(self, left, right)
                self.childNodes.append(temp)
            if(self.leftBank[1] >= 2):
                left = self.leftBank.copy()
                left[1] = left[1] - 2
                left[2] = 0
                right = self.rightBank.copy()
                right[1] = right[1] + 2
                right[2] = 1
                temp = Node(self, left, right)
                self.childNodes.append(temp)
            if(self.leftBank[0] >= 1 and self.leftBank[1] >= 1):
                left = self.leftBank.copy()
                left[0] = left[0] - 1
                left[1] = left[1] - 1
                left[2] = 0
                right = self.rightBank.copy()
                right[0] = right[0] + 1
                right[1] = right[1] + 1
                right[2] = 1
                temp = Node(self, left, right)
                self.childNodes.append(temp)
        else:
            if(self.rightBank[0] >= 1):
                left = self.leftBank.copy()
                left[0] = left[0] + 1
                left[2] = 1
                right = self.rightBank.copy()
                right[0] = right[0] - 1
                right[2] = 0
                temp = Node(self, left, right)
                self.childNodes.append(temp)
            if(self.rightBank[0] >= 2):
                left = self.leftBank.copy()
                left[0] = left[0] + 2
                left[2] = 1
                right = self.rightBank.copy()
                right[0] = right[0] - 2
                right[2] = 0
                temp = Node(self, left, right)
                self.childNodes.append(temp)
            if(self.rightBank[1] >= 1):
                left = self.leftBank.copy()
                left[1] = left[1] + 1
                left[2] = 1
                right = self.rightBank.copy()
                right[1] = right[1] - 1
                right[2] = 0
                temp = Node(self, left, right)
                self.childNodes.append(temp)
            if(self.rightBank[1] >= 2):
                left = self.leftBank.copy()
                left[1] = left[1] + 2
                left[2] = 1
                right = self.rightBank.copy()
                right[1] = right[1] - 2
                right[2] = 0
                temp = Node(self, left, right)
                self.childNodes.append(temp)
            if(self.rightBank[0] >= 1 and self.rightBank[1] >= 1):
                left = self.leftBank.copy()
                left[0] = left[0] + 1
                left[1] = left[1] + 1
                left[2] = 1
                right = self.rightBank.copy()
                right[0] = right[0] - 1
                right[1] = right[1] - 1
                right[2] = 0
                temp = Node(self, left, right)
                self.childNodes.append(temp)
        if(len(self.childNodes) > 0):
            return True
        else:
            return False

    def validate(self):
        for n in list(self.childNodes):
            if(((n.leftBank[0] < n.leftBank[1]) and n.leftBank[0] != 0) or (n.rightBank[0] < n.rightBank[1] and (n.rightBank[0] != 0))):
                self.childNodes.remove(n)

    def printNode(self):
        print('Left Shore: ', self.leftBank, 'Right Shore: ', self.rightBank)

    def printchildren(self):
        for n in self.childNodes:
            n.printNode()
