# Assignment-2
#Explaination

In this assignment, I solved the problem of finding a path in an n × n binary matrix using two algorithms:
1.Best First Search (Greedy Search)
2.A Search*

🔹 Problem Description
. The grid is an n × n binary matrix.
. A cell with 0 is free, and 1 is blocked.
. The task is to find a path from the top-left (0,0) to the bottom-right (n-1,n-1).
. Movement is allowed in 8 directions (horizontal, vertical, diagonal).
. The path length is the number of visited cells.

🔹 Approach
1. Best First Search
I used a Greedy Search strategy with Euclidean distance as the heuristic.
It always expands the node closest to the goal (by heuristic), but it does not guarantee the shortest path.
If a path exists, it records the sequence of coordinates and path length.
If no path exists, it returns -1.

2. A* Search
I implemented the A algorithm* with the same heuristic.
A* combines:
g(n): cost from the start to the current node
h(n): heuristic distance to the goal
f(n) = g(n) + h(n)
This ensures it finds the shortest path if one exists.
If no path exists, it also returns -1.
