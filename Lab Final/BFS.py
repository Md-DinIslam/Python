import math
import heapq
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def check(i, j, n, m, vis, graph):
        return (i >= 0 and i < n and j >= 0 and j < m and graph[i][j] == 1 and vis[i][j] == 0)

def solve():
        # n = int(input("Enter Board Size: "))
        # graph = [[0 for _ in range(n)] for _ in range(m)]

        graph = [[1, 0, 'S', 0, 1],
           [1, 0, 1, 0, 1],
           [1, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 0, 1, 1, 'G']]

        n = len(graph)
        m = len(graph[0])

        si = sj = ei = ej = -1
        for i in range(n):
                for j in range(m):
                        if (graph[i][j] == 'S'):
                                si = i
                                sj = j
                        if (graph[i][j] == 'G'):
                                ei = i
                                ej = j
                                graph[i][j] = 1

        print(si, sj, ei, sj)

        q = deque()
        vis = [[0 for _ in range(n)] for _ in range(m)]

        q.append((si, sj))
        vis[si][sj] = 1

        while q:
                i, j = q.popleft()
                print(i, j, ":", graph[i][j])
                if (i == ei and j == ej):
                        return
                for k in range(4):
                        ni = dx[k] + i
                        nj = dy[k] + j
                        if (check(ni, nj, n, m, vis, graph)):
                                q.append((ni, nj))
                                vis[ni][nj] = 1
        

if __name__ == '__main__':
        solve()
