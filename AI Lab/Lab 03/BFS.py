from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def check(i, j, n, m, vis, adj):
    return (i >= 0 and i < n and j >= 0 and j < m and vis[i][j] == False and (adj[i][j] == 1 or adj[i][j] == 'G'))

def BFS():
    # print("test")
    # n = int(input("Enter Row: "))
    # m = int(input("Enter Column:"))
    # adj = [[0 for _ in range(m + 1)] for _ in range(n+1)]
    # for i in range(1, n+1):
    #     print("Enter ", i, "th rows values")
    #     for j in range(1, m+1):
    #         adj[i][j] = int(input())

    adj = [[1, 0, 'S', 0, 1],
           [1, 0, 1, 0, 1],
           [1, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 0, 1, 1, 'G']]
    n = 5
    m = 5
    
    print("Matrix:")
    si = sj = ei = ej = 4
    for i in range(n):
        for j in range(m):
            if (adj[i][j] == 'S'):
                si = i
                sj = j
            if (adj[i][j] == 'G'):
                ei = i
                ej = j
            print(adj[i][j], end=" ")
        print()

    q = deque()
    vis = [[False for _ in range(m)] for _ in range(n)]

    q.append((si, sj))
    vis[si][sj] = True

    while q:
        i, j = q.popleft()
        print("R:", i, "C:", j, "Adj:", adj[i][j])
        if i == ei and j == ej:
            break
        for k in range(4):
            new_i = dx[k] + i
            new_j = dy[k] + j
            if check(new_i, new_j, n, m, vis, adj):
                q.append((new_i, new_j))
                vis[new_i][new_j] = True


if __name__ == "__main__":
    BFS()