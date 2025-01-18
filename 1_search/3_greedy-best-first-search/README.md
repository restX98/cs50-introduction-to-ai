# Greedy Best-First Search

Breadth-first and depth-first are both **uninformed** search algorithms.
These algorithms do not utilize any knowledge about the problem that they did not acquire through their own exploration.

However, most often is the case that some knowledge about the problem is, in fact, available. For example, when a human maze-solver enters a junction, the human can see which way goes in the general direction of the solution and which way does not.

AI can do the same and a type of algorithm that considers additional knowledge to try to improve its performance is called an informed search algorithm.

**Greedy best-first** search expands the node that is the closest to the goal, as determined by a **heuristic function** `h(n)`.

The heuristic function estimates how close to the goal the next node is, but it can be mistaken.

The efficiency of the greedy best-first algorithm depends on how good the heuristic function is.

An example of heuristic function is the **Manhattan discance** that ignores walls and counts how many steps up, down, or to the sides it would take to get from one location to the goal location.

However, it is important to emphasize that, as with any heuristic, it can go wrong and lead the algorithm down a slower path than it would have gone otherwise.

#### Note
It is possible that an uninformed search algorithm will provide a better solution faster, but it is less likely to do so than an informed algorithm.

