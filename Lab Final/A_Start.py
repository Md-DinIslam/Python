import math
import heapq

def a_star(start, goal, n, graph, heuristic):
        pq = []
        heapq.heappush(pq, (heuristic[start], 0, start))

        g_cost = [math.inf] * n
        g_cost[start] = 0

        parent = [-1] * n
        vis = [0] * n

        while pq:
                f, g, node = heapq.heappop(pq) # f(n), g(n), curr_node...
                if vis[node] == 1:
                        continue
                vis[node] = 1

                if node == goal: # target found...
                        path = []
                        while (node != -1):
                                path.append(node)
                                node = parent[node]
                        path.reverse()
                        return path
                
                for child in range(n):
                        cost = graph[node][child]
                        if (cost > 0 and vis[child] == 0):
                                new_g = g + cost
                                if (new_g < g_cost[child]):
                                        g_cost[child] = new_g
                                        parent[child] = node
                                        f_cost = new_g + heuristic[child]
                                        heapq.heappush(pq, (f_cost, new_g, child))
        return None

def solve():
        # n = int(input("Enter Board Size: "))
        n = 7
        m = 7

        # graph = [[0 for _ in range(n)] for _ in range(m)]
        graph = [
                [0, 6, 2, 0, 0, 0, 10],
                [6, 0, 3, 1, 0, 0, 0],
                [2, 3, 0, 0, 6, 2, 0],
                [0, 1, 0, 0, 4, 0, 0],
                [0, 0, 6, 4, 0, 3, 0],
                [0, 0, 2, 0, 3, 0, 1],
                [10, 0, 0, 0, 0, 1, 0]
        ]

        heuristic = [5, 3, 3, 2, 6, 3, 0]

        start = 0
        goal = 6

        path = a_star(start, goal, n, graph, heuristic)

        if path:
                print("Found: ", path)
        else:
                print("Not Found.")

if __name__ == '__main__':
        solve()
