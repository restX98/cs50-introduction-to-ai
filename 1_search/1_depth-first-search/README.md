# Depth First Search (DFS)

A depth-first search algorithm exhausts each one direction before trying another direction.

In these cases, the frontier is managed as a stack data structure.

This results in a search algorithm that goes as deep as possible in the first direction that gets in its way while leaving all other directions for later.

### Pros:

- At best, this algorithm is the fastest. If it “lucks out” and always chooses the right path to the solution (by chance), then depth-first search takes the least possible time to get to a solution.

### Cons:

- It is possible that the found solution is not optimal.

- At worst, this algorithm will explore every possible path before finding the solution, thus taking the longest possible time before reaching the solution.