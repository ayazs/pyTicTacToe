

class tttBoard:
    # arBoard = [[0,0,0],[0,0,0],[0,0,0]]
    boardAvail = set((x,y) for x in range(0,2) for y in range(0,2))
    boardPlayed = [set(),set()]
    
    def __init__(self, board = None):
        if (board is not None):
            self.boardAvail = board.boardAvail.copy()
            self.boardPlayed[0] = board.boardPlayed[0].copy()
            self.boardPlayed[1] = board.boardPlayed[1].copy()

    def __repr__(self):
        return "<tttBoard boardAvail:{} boardPlayed:{} >".format(self.boardAvail, self.boardPlayed)
    
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
            s = (x,y)
            retVal.boardAvail.remove(s)
            retVal.boardPlayed[player-1].add(s)
            return retVal
        except:
            raise
        
    def getPos(self, x, y):
        try:
            s = (x,y)
            if s in boardAvail:
                return 0
            elif s in boardPlayed[0]:
                return 1
            elif s in boardPlayed[1]:
                return 2
            else:
                raise ValueError("Coordinates ({}) are invalid.".format(s))
        except:
            raise
    
    def isPlayable(self, x = -1, y = -1):
        if ((x == -1) and (y == -1)):
            return True if len(self.boardAvail) > 0 else False
        else:
            s = (x,y)
            if s in self.boardAvail:
                return True

        return False
        
    def getNextAvail(self):
        return None if len(self.boardAvail) == 0 else next(iter(self.board))
        

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
        
        #while s = board.getNextAvail():
            
        
        for x in range (0,2):
            for y in range (0,2):
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
    