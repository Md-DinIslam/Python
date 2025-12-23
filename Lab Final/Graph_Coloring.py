import math

def isSafe(node, n, curr_color, graph, assignment):
        for child in range(n):
                if (graph[node][child] == 1 and assignment[child] == curr_color):
                        return 0
        return 1


def mapColoring(node, n, graph, colors, assignment):
        if (node >= n): # base case
                return 1
        for curr_color in colors:
                if (isSafe(node, n, curr_color, graph, assignment) == 1):
                        assignment[node] = curr_color
                        if (mapColoring(node + 1, n, graph, colors, assignment) == 1):
                                return 1
                        assignment[node] = None # backtrace...
        
        return 0

def solve():
        # user input... 
        # n = int(input("Enter Board Size: "))
        # graph = [[0 for _ in range(n)] for _ in range(n)]

        n = 7
        m = 7

        graph = [
                [0, 1, 1, 0, 0, 0, 0],
                [1, 0, 1, 1, 0, 0, 0],
                [1, 1, 0, 1, 1, 1, 0],
                [0, 1, 1, 0, 1, 0, 0],
                [0, 0, 1, 1, 0, 1, 0],
                [0, 0, 1, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0]
        ]

        colors = ["Red", "Green", "Blue"]
        assignment = [None] * n

        # input matrix of graph...
        # for i in range(n):
        #         for j in range(m):
        #                 graph[i][j] = int(input())
        
        # print graph....
        # for i in range(n):
        #         for j in range(m):
        #                 print(graph[i][j], end=" ")
        #         print()

        if (mapColoring(0, n, graph, colors, assignment) == 1):
                print("Colors: ", end=" ")
                for color in assignment:
                        print(color, end=" ")
                print()
        else:
                print("No Solution Exist.")
        

if __name__ == '__main__':
        solve()
