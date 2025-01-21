# 1. Search

## Intro

Search problems involve an agent that is given an initial state and a goal state, and it returns a solution of how to get from the former to the latter. A navigator app uses a typical search process, where the agent (the thinking part of the program) receives as input your current location and your desired destination, and, based on a search algorithm, returns a suggested path. However, there are many other forms of search problems, like puzzles or mazes.

## Components


### Agent
 An entity that perceives its environment and acts upon that environment. In a navigator app, for example, the agent would be a representation of a car that needs to decide on which actions to take to arrive at the destination.

### State
 A configuration of an agent in its environment. For example, in a 15 puzzle, a state is any one way that all the numbers are arranged on the board.

### Initial State
 The state from which the search algorithm starts. In a navigator app, that would be the current location.

### Actions
 Choices that can be made in a state. More precisely, actions can be defined as a function. Upon receiving state `s` as input, `Actions(s)` returns as output the set of actions that can be executed in state `s`. For example, in a 15 puzzle, the actions of a given state are the ways you can slide squares in the current configuration (4 if the empty square is in the middle, 3 if next to a side, 2 if in the corner).

### Transition Model
 A description of what state results from performing any applicable action in any state. More precisely, the transition model can be defined as a function. Upon receiving state `s` and action `a` as input, `Results(s, a)` returns the state resulting from performing action `a` in state `s`. For example, given a certain configuration of a 15 puzzle (state `s`), moving a square in any direction (action `a`) will bring to a new configuration of the puzzle (the new state).

### State Space
 The set of all states reachable from the initial state by any sequence of actions. For example, in a 15 puzzle, the state space consists of all the 16!/2 configurations on the board that can be reached from any initial state. The state space can be visualized as a directed graph with states, represented as nodes, and actions, represented as arrows between nodes.


### Goal Test
 The condition that determines whether a given state is a goal state. For example, in a navigator app, the goal test would be whether the current location of the agent (the representation of the car) is at the destination. If it is — problem solved. If it’s not — we continue searching.

### Path Cost
 A numerical cost associated with a given path. For example, a navigator app does not simply bring you to your goal; it does so while minimizing the path cost, finding the fastest way possible for you to get to your goal state.

## Solving Search Problems

### Solution
 A sequence of actions that leads from the initial state to the goal state.

### Optimal Solution
 A solution that has the lowest path cost among all solutions.

In a search process, data is often stored in a node, a data structure that contains the following data:

- A state
- Its parent node, through which the current node was generated
- The action that was applied to the state of the parent to get to the current node
- The path cost from the initial state to this node

Nodes are simply a data structure, they don’t search, they hold information. To actually search, we use the **frontier**, the mechanism that “manages” the nodes. The **frontier** starts by containing an initial state and an empty set of explored items, and then repeats the following actions until a solution is reached:

#### Repeat:
```
1. If the frontier is empty:
    Stop. There is no solution to the problem.

2. Remove a node from the frontier. This is the node that will be considered.

3.If the node contains the goal state:
    Return the solution. Stop.
Else:
    3.1. Expand the node (find all the new nodes that could be reached from this node), and add resulting nodes to the frontier.
    
    3.2. Add the current node to the explored set.
```

## Uninformed and Informed Search Algorithm

### Uninformed Search
Uninformed search algorithms (also called blind search algorithms) do not have additional information about the problem's domain other than the definition of the goal and the operators.

These algorithms explore the search space systematically but without guidance, often leading to inefficiency.

Examples: Breadth-First Search (BFS) and Depth-First Search (DFS).

### Informed Search
Informed search algorithms (also called heuristic search algorithms) use additional knowledge about the problem to guide the search towards the goal more efficiently.

This knowledge is typically provided in the form of a heuristic function, which estimates the cost to reach the goal from a given state. 

Examples: A* and Greedy Best-First Search.

# Adversarial Search

The adversarial search algorithm faces an opponent that tries to achieve the opposite goal.
