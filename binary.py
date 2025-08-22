import heapq
import math

directions=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def heuristic(a,b):
    return math.dist(a,b)

def best_first_search(grid):
    n=len(grid)
    if grid[0][0]==1 or grid[n-1][n-1]==1:
        return -1,[]
    pq=[(heuristic((0,0),(n-1,n-1)),(0,0),[(0,0)])]
    visited=set([(0,0)])
    while pq:
        _,(x,y),path=heapq.heappop(pq)
        if (x,y)==(n-1,n-1):
            return len(path),path
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<n and grid[nx][ny]==0 and (nx,ny) not in visited:
                visited.add((nx,ny))
                heapq.heappush(pq,(heuristic((nx,ny),(n-1,n-1)),(nx,ny),path+[(nx,ny)]))
    return -1,[]

def a_star_search(grid):
    n=len(grid)
    if grid[0][0]==1 or grid[n-1][n-1]==1:
        return -1,[]
    pq=[(heuristic((0,0),(n-1,n-1)),0,(0,0),[(0,0)])]
    g={(0,0):0}
    while pq:
        f,cost,(x,y),path=heapq.heappop(pq)
        if (x,y)==(n-1,n-1):
            return len(path),path
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<n and grid[nx][ny]==0:
                new_cost=cost+1
                if (nx,ny) not in g or new_cost<g[(nx,ny)]:
                    g[(nx,ny)]=new_cost
                    heapq.heappush(pq,(new_cost+heuristic((nx,ny),(n-1,n-1)),new_cost,(nx,ny),path+[(nx,ny)]))
    return -1,[]

grids=[
    [[0,1],[1,0]],
    [[0,0,0],[1,1,0],[1,1,0]],
    [[1,0,0],[1,1,0],[1,1,0]]
]

for grid in grids:
    bf_len,bf_path=best_first_search(grid)
    a_len,a_path=a_star_search(grid)
    print("Best First Search → Path length:",bf_len,"Path:",bf_path)
    print("A* Search → Path length:",a_len,"Path:",a_path)
    print()

