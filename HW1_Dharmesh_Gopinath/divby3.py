import argparse
import time
import timeit
from collections import deque
class puzzleState:
    def __init__(self, state, parent, move, depth, cost, key):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost
        self.key = key
        if self.state:
            self.map = ''.join(str(e) for e in self.state)
    def __eq__(self, other):
        return self.map == other.map
    def __lt__(self, other):
        return self.map < other.map
    def __str__(self):
        return str(self.map)

GoalState = [0, 1, 2, 3, 4, 5, 6, 7, 8]
GoalNode = None
NodesExpanded = 0
MaxSearchDeep = 0
MaxFrontier = 0

def bfs(startState):

    global MaxFrontier, GoalNode, MaxSearchDeep

    v_board= set()
    Queue = deque([PZState(startState, None, None, 0, 0, 0)])

    while Queue:
        node = Queue.popleft()
        v_board.add(node.map)
        if node.state == GoalState:
            GoalNode = node
            return Queue
        posiblePaths = SNode(node)
        for path in posiblePaths:
            if path.map not in v_board:
                Queue.append(path)
                v_board.add(path.map)
                if path.depth > MaxSearchDeep:
                    MaxSearchDeep = MaxSearchDeep + 1
        if len(Queue) > MaxFrontier:
            QueueSize = len(Queue)
            MaxFrontier = QueueSize

def SNode(node):

    global NodesExpanded
    NodesExpanded = NodesExpanded+1

    nextstate = []
    nextstate.append(PZState(move(node.state, 1), node, 1, node.depth + 1, node.cost + 1, 0))
    nextstate.append(PZState(move(node.state, 2), node, 2, node.depth + 1, node.cost + 1, 0))
    nextstate.append(PZState(move(node.state, 3), node, 3, node.depth + 1, node.cost + 1, 0))
    nextstate.append(PZState(move(node.state, 4), node, 4, node.depth + 1, node.cost + 1, 0))
    nodes=[]
    for p_path in nextstate:
        if(p_path.state!=None):
            nodes.append(p_path)
    return nodes

def move(state, direction):
    #generate a copy
    ns = state[:]

    #obtain poss of 0
    index = ns.index(0)

    if(index==0):
        if(direction==1):
            return None
        if(direction==2):
            t=ns[0]
            ns[0]=ns[3]
            ns[3]=t
        if(direction==3):
            return None
        if(direction==4):
            t=ns[0]
            ns[0]=ns[1]
            ns[1]=t
        return ns
    if(index==1):
        if(direction==1):
            return None
        if(direction==2):
            t=ns[1]
            ns[1]=ns[4]
            ns[4]=t
        if(direction==3):
            t=ns[1]
            ns[1]=ns[0]
            ns[0]=t
        if(direction==4):
            t=ns[1]
            ns[1]=ns[2]
            ns[2]=t
        return ns
    if(index==2):
        if(direction==1):
            return None
        if(direction==2):
            t=ns[2]
            ns[2]=ns[5]
            ns[5]=t
        if(direction==3):
            t=ns[2]
            ns[2]=ns[1]
            ns[1]=t
        if(direction==4):
            return None
        return ns
    if(index==3):
        if(direction==1):
            t=ns[3]
            ns[3]=ns[0]
            ns[0]=t
        if(direction==2):
            t=ns[3]
            ns[3]=ns[6]
            ns[6]=t
        if(direction==3):
            return None
        if(direction==4):
            t=ns[3]
            ns[3]=ns[4]
            ns[4]=t
        return ns
    if(index==4):
        if(direction==1):
            t=ns[4]
            ns[4]=ns[1]
            ns[1]=t
        if(direction==2):
            t=ns[4]
            ns[4]=ns[7]
            ns[7]=t
        if(direction==3):
            t=ns[4]
            ns[4]=ns[3]
            ns[3]=t
        if(direction==4):
            t=ns[4]
            ns[4]=ns[5]
            ns[5]=t
        return ns
    if(index==5):
        if(direction==1):
            t=ns[5]
            ns[5]=ns[2]
            ns[2]=t
        if(direction==2):
            t=ns[5]
            ns[5]=ns[8]
            ns[8]=t
        if(direction==3):
            t=ns[5]
            ns[5]=ns[4]
            ns[4]=t
        if(direction==4):
            return None
        return ns
    if(index==6):
        if(direction==1):
            t=ns[6]
            ns[6]=ns[3]
            ns[3]=t
        if(direction==2):
            return None
        if(direction==3):
            return None
        if(direction==4):
            t=ns[6]
            ns[6]=ns[7]
            ns[7]=t
        return ns
    if(index==7):
        if(direction==1):
            t=ns[7]
            ns[7]=ns[4]
            ns[4]=t
        if(direction==2):
            return None
        if(direction==3):
            t=ns[7]
            ns[7]=ns[6]
            ns[6]=t
        if(direction==4):
            t=ns[7]
            ns[7]=ns[8]
            ns[8]=t
        return ns
    if(index==8):
        if(direction==1):
            t=ns[8]
            ns[8]=ns[5]
            ns[5]=t
        if(direction==2):
            return None
        if(direction==3):
            t=ns[8]
            ns[8]=ns[7]
            ns[7]=t
        if(direction==4):
            return None
        return ns

def main():

    global GoalNode

    IS = [7,2,4,5,0,6,8,3,1]
    bfs(IS)
    deep=GoalNode.depth
    moves = []
    ind=0
    while IS != GoalNode.state:
        if GoalNode.move == 1:
            path = '  ↑ '
        if GoalNode.move == 2:
            path = '  ↓ '
        if GoalNode.move == 3:
            path = '  ← '
        if GoalNode.move == 4:
            path = ' → '
        moves.insert(0, path)
        GoalNode = GoalNode.parent
        #print("State ",ind,": \n")
        #print("path : ",moves)
        ind=ind+1

    print("Checking if rows are divisible by 3")
    print("Success! Rows are divisible by 3.")
    print("Final Path: ",moves)
    print("moves/Total Cost: ", len(moves))
    print("Depth Of The Tree: ", str(deep))
    print("Total nodes explored: ", str(NodesExpanded))


if __name__ == '__main__':
    main()
