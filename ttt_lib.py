

class tttBoard:
    arBoard = [[0,0,0],[0,0,0],[0,0,0]]
    # boardAvail = set((x,y) for x in range(0,3) for y in range(0,3))
    # boardX = set()
    # boardY = set()
    
    def __init__(self, board = None):
        if (board is not None):
            for x in range(0,3):
                for y in range (0,3):
                    self.arBoard[x][y] = board.arBoard[x][y]
                    
    # def __repr__(self):
    #     return "<tttBoard arBoard:%s>" % (self.arBoard)
    
    def copy(self):
        newBoard = tttBoard(self)
        return newBoard        
    
    def playPos(self, player, x, y):
        if player not in range (1,3):
            raise ValueError("Player {} is invalid".format(player))
        try:
            if not self.isPlayable(x,y):
                return None
            retVal = self.copy()
            retVal.arBoard[x][y] = player
            return retVal
        except:
            raise
        
    def getPos(self, x, y):
        try:
            return self.arBoard[x][y]
        except:
            raise
    
    def isPlayable(self, x = -1, y = -1):
        if ((x == -1) and (y == -1)):
            for val in self.arBoard:
                if val == 0:
                    return True
        elif (x == -1):
            for n in range(0,3):
                if self.arBoard[n][y] == 0:
                    return True
            return False
        elif (y == -1):
            for n in range(0,3):
                if self.arBoard[x][n] == 0:
                    return True
            return False
        else:
            if self.arBoard[x][y] == 0:
                return True

        return False
        
        

class tttTreeNode:
    nodeParent = object
    nodeChildren = []
    nodeBoard = tttBoard()
    
    def __init__(self, parentNode = None, board = None):
        # if (parentNode != None) and (parentNode is not tttTreeNode):
        #     raise TypeError("Parent must be a tttTreeNode or None")
        self.nodeParent = parentNode
        
        # if (board is not None) and (board is not tttBoard):
        #     raise TypeError("Board must be a tttBoard or None")
        # elif (board is not None):
        #     self.nodeBoard = board
        if (board is not None):
            self.nodeBoard = board
            
    def __repr__(self):
        return "<tttTreeNode nodeBoard:%s>" % (self.nodeBoard)
        
    def getBoard(self):
        return self.nodeBoard
    
    def seed(self, turn=1):
        board = self.getBoard()
        
        for x in range (0,3):
            for y in range (0,3):
                print("In seed() [{}][{}] turn={}. I am: {}".format(x,y,turn,self))

                newBoard = board.playPos(turn,x,y)
                if newBoard == None:
                    continue
                
                childTree = tttTreeNode(self,newBoard)
                self.nodeChildren.append(childTree)
                newTurn = 2 if turn == 1 else 1
                childTree.seed(newTurn)
                
theTree = tttTreeNode()
print("Created theTree: {}".format(theTree))

theTree.seed()
    
print(theTree)
    