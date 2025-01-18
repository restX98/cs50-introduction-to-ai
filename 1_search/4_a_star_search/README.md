# A* Search

A development of the greedy best-first algorithm, A* search considers not only `h(n)`, the estimated cost from the current location to the goal, but also `g(n)`, the cost that was accrued until the current location.

By combining both these values, the algorithm has a more accurate way of determining the cost of the solution and optimizing its choices on the go.

The algorithm keeps track of (cost of path until now + estimated cost to the goal), and once it exceeds the estimated cost of some previous option, the algorithm will ditch the current path and go back to the previous option, thus preventing itself from going down a long, inefficient path that `h(n)` erroneously marked as best.


For A* search to be optimal, the heuristic function, `h(n)`, should be:

- Admissible: never overestimating the true cost
- Consistent: h(n) is consistent if $h(n) ≤ h(n') + c(n, n')$. Which means that the estimated path cost to the goal of a new node ($h(n')$) in addition to the cost of transitioning to it from the previous node ($c(n, n')$) is greater or equal to the estimated path cost to the goal of the previous node ($h(n)$).

#### Note
There are some math property for heuristic function.