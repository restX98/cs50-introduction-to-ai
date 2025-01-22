# Minimax

Minimax is a type of algorithm in adversarial search, represents winning conditions as (-1) for one side and (+1) for the other side. Further actions will be driven by these conditions, with the minimizing side trying to get the lowest score, and the maximizer trying to get the highest score.


## Representing a Tic-Tac-Toe AI:

- `S₀`: Initial state (in our case, an empty 3X3 board)
- `Players(s)`: a function that, given a state s, returns which player’s turn it is (X or O).
- `Actions(s)`: a function that, given a state s, return all the legal moves in this state (what spots are free on the board).
- `Result(s, a)`: a function that, given a state s and action a, returns a new state. This is the board that resulted from performing the action a on state s (making a move in the game).
- `Terminal(s)`: a function that, given a state s, checks whether this is the last step in the game, i.e. if someone won or there is a tie. Returns True if the game has ended, False otherwise.
- `Utility(s)`: a function that, given a terminal state s, returns the utility value of the state: -1, 0, or 1.


Recursively, the algorithm simulates all possible games that can take place beginning at the current state and until a terminal state is reached. Each terminal state is valued as either (-1), 0, or (+1).

## Pseudocode

```
Given a state s:
    1.a The maximizing player picks action a in Actions(s) that produces the highest value of Min-Value(Result(s, a)).
    1.b The minimizing player picks action a in Actions(s) that produces the lowest value of Max-Value(Result(s, a)).


Function Max-Value(state):
    value = -∞
    
    if Terminal(state):
        return Utility(state)

    for action in Actions(state):
         value = max(v, Min-Value(Result(state, action)))

Function Min-Value(state):
    value = ∞
    
    if Terminal(state):
        return Utility(state)

    for action in Actions(state):
         value = min(v, Max-Value(Result(state, action)))

```

# Depth-Limited Minimax

Depth-limited Minimax considers only a pre-defined number of moves before it stops, without ever getting to a terminal state. However, this doesn’t allow for getting a precise value for each action, since the end of the hypothetical games has not been reached. To deal with this problem, Depth-limited Minimax relies on an evaluation function that estimates the expected utility of the game from a given state, or, in other words, assigns values to states. For example, in a chess game, a utility function would take as input a current configuration of the board, try to assess its expected utility (based on what pieces each player has and their locations on the board), and then return a positive or a negative value that represents how favorable the board is for one player versus the other.