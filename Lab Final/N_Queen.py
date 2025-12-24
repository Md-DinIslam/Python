import math

def canPlace(i, j, board, n):
        # column check..
        for k in range(0, i):
                if (board[k][j] == 1):
                        return 0
        # left diagonal..
        x = i
        y = j
        while (x >= 0 and y >= 0):
                if (board[x][y] == 1):
                        return 0
                x -= 1
                y -= 1
        # right diagonal..
        x = i
        y = j
        while (x >= 0 and y < n):
                if (board[x][y] == 1):
                        return 0
                x -= 1
                y += 1
        return 1

def nQueen(i, n, board, all_distinct):
        if (i >= n):
                # all_distinct.append([row[:] for row in board])
                all_distinct.append(list(map(list, board)))
                return 1
        
        for j in range(0, n):
                if (canPlace(i, j, board, n)):
                        board[i][j] = 1
                        ok = nQueen(i+1, n, board, all_distinct)
                        # if (ok == 1): # only for one solution...
                        #         return 1
                        board[i][j] = 0 # backtrack...
        return 0


def solve():
        # n = int(input("Enter Board Size: "))
        n = 4
        board = [[0 for _ in range(n)] for _ in range(n)]
        all_distinct = []
        nQueen(0, n, board, all_distinct)

        # for i in range(0, n): # one solution...
        #         for j in range(0, n):
        #                 print(board[i][j], end=" ")
        #         print()

        cnt = 0
        for ans in all_distinct:
                cnt += 1
                print("Solution: ", cnt)
                for row in ans:
                        for col in row:
                                print(col, end=" ")
                        print()
                print()

if __name__ == '__main__':
        solve()
