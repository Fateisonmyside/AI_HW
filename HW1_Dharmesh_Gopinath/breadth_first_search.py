import math
from collections import deque


class State:  ## State Definition #####################################################
    def __init__(self, state, parent, action, depth, cost):
        self.state = state  # the state
        self.parent = parent  # parent state
        self.action = action  # the action lead to this state
        self.depth = depth  # parent.depth +1
        self.cost = cost  # associated cost
        if self.state:
            self.map = ''.join(str(e) for e in self.state)

        def __eq__(self, other):
            return self.map == other.map

        def __lt__(self, other):
            return self.map < other.map

        def __str__(self):
            return str(self.map)

        def __cmp__(self, other):
            return (self.cost, other.cost)


def next_state(state, action):  ## The state after each action   #################################################
    current_State = str(state.state[:])
    #print("Alt: ",state)
    count = (current_State.index('0')) + 1
    empty_row = math.ceil(count / 3)
    empty_cols = count - ((empty_row - 1) * 3)
    empty_count = count

    output_state = ""
    if action == 1:  # 1: moving up
        cost = 1
        if empty_row == 3:
            output_state = current_State
        else:
            for i in range(0, 9):
                if i == (empty_count - 1):
                    output_state += current_State[empty_count + 2]
                elif i == (empty_count + 2):
                    output_state += current_State[empty_count - 1]
                else:
                    output_state += current_State[i]

    elif action == 2:  # 2: down
        cost = 1
        if empty_row == 1:
            output_state = current_State
        else:
            for i in range(0, 9):
                if i == (empty_count - 1):
                    output_state += current_State[empty_count - 4]
                elif i == (empty_count - 4):
                    output_state += current_State[empty_count - 1]
                else:
                    output_state += current_State[i]

    elif action == 3:  # 3: left
        cost = 2
        if empty_cols == 3:
            output_state = current_State
        else:
            for i in range(0, 9):
                if i == (empty_count - 1):
                    output_state += current_State[empty_count]
                elif i == (empty_count):
                    output_state += current_State[empty_count - 1]
                else:
                    output_state += current_State[i]

    elif action == 4:  # 4: right
        cost = 0.5
        if empty_cols == 1:
            output_state = current_State
        else:
            for i in range(0, 9):
                if i == (empty_count - 1):
                    output_state += current_State[empty_count - 2]
                elif i == (empty_count - 2):
                    output_state += current_State[empty_count - 1]
                else:
                    output_state += current_State[i]

    output_state = State(output_state, state, action, state.depth + 1, cost)
    return output_state




## Breadth First Algorithm      #####################################################################################

def breadth_first_search(intial_state, goal_state):
    open_states = deque([State(intial_state, None, None, 0, 0)])
    closed_states = set()

    counter = 0

    while (len(open_states) != 0):
        current_state = open_states.popleft()
        closed_states.add(current_state.map)
        Goal = False

        # checking childs of current state
        for action in range(1, 5):
            child = next_state(current_state, action)
            # if (child not in open_states):      # this check significantly decreases the computing speed, and it is not affecting the result
            if (child.map not in closed_states):
                if (child.state == goal_state):
                    print("Success! The number of iterations =", counter, ", The size of the closed states:",
                          len(closed_states))
                    Goal = True
                    break
                else:
                    open_states.append(child)
            counter += 1
            if (counter % 100000 == 0):
                print("Iterations: ", counter, ", The size of the closed states:", len(closed_states))
        if Goal == True:
            break
        if (len(open_states) == 0):
            print("All the open states are consumed with no solution")
    if Goal == True:
        return child





## Main                         #####################################################################################

def main(InitialState, GoalState):
    print("Initial State: ", InitialState)
    print("Goal State: ", GoalState)

    AchievedGoal = breadth_first_search(InitialState, GoalState)

    Depth = AchievedGoal.depth

    Path = []
    i = 0
    while InitialState != AchievedGoal.state:
        action = AchievedGoal.action
        if action == 1:
            move = 'Up'
        if action == 2:
            move = 'Down'
        if action == 3:
            move = 'Left'
        if action == 4:
            move = 'Right'

        if Depth > 50:
            i += 1
            if i <= 6:
                Path.insert(0, [AchievedGoal.state, move])
            elif i <= 10:
                Path.insert(0, "..")
            elif i > (Depth - 6):
                Path.insert(0, [move, AchievedGoal.state])
        else:
            Path.insert(0, [move, AchievedGoal.state])

        AchievedGoal = AchievedGoal.parent

    Path.insert(0, [AchievedGoal.state])

    print("Depth aka the number of actions = ", Depth)
    print("The actions and states (the path) are: ", Path)


## User Input                   #####################################################################################

InitialState = '724506831'  # the intial state of the puzzle from top left to bottom right
GoalState = '012345678'  # the goal state of the puzzle from top left to bottom right
#The Search Type is breadth-first search.

if __name__ == "__main__":
    main(InitialState, GoalState)