#https://www.acmicpc.net/problem/2210
from collections import deque

def solve():
    graph = []
    values =set()
    
    stack = deque()
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]

    for _ in range(5):
        graph.append(list(input().split()))
    
    for i in range(5):
        for j in range(5):
            stack.append((i,j,graph[i][j]))
            while (stack):
                x,y,val = stack.pop()
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if 0<=nx<5 and 0<=ny<5 and len(val)<6:
                        temp= val + graph[nx][ny]
                        stack.append((nx,ny,temp))
                if len(val) == 6:
                    values.add(val)
    
    # print(values)
    print(len(values))
  
    return

if __name__ == "__main__":
    solve()