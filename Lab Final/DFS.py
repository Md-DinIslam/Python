import math
import heapq
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def check(i, j, n, m, vis, graph):
        return (i >= 0 and i < n and j >= 0 and j < m and graph[i][j] == 1 and vis[i][j] == 0)

def dfs(x, y, n, m, vis, graph, parent, ei, ej):
        vis[x][y] = 1
        if (x == ei and y == ej):
                return 1

        for k in range(4):
                ni = dx[k] + x
                nj = dy[k] + y
                if (check(ni, nj, n, m, vis, graph)):
                        parent[ni][nj] = (x, y)
                        if (dfs(ni, nj, n, m, vis, graph, parent, ei, ej)):
                                return 1
        
        return 0
        

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

        vis = [[0 for _ in range(m)] for _ in range(n)]
        parent = [[None for _ in range(m)] for _ in range(n)]

        # dfs(si, sj, n ,m, vis, graph, parent, ei, ej)

        if dfs(si, sj, n ,m, vis, graph, parent, ei, ej):
                path = []
                node = (ei, ej)
                while node:
                        path.append(node)
                        node = parent[node[0]][node[1]]
                path.reverse()
                print("Path: ", path)
        else:
                print("No path.")

if __name__ == '__main__':
        solve()
