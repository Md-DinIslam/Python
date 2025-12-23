import math

node_evaluate = 0

def minmax(indx, curr_depth, turn, arr, target_depth):
        # print()
        global node_evaluate
        node_evaluate += 1
        
        if (curr_depth == target_depth):
                return arr[indx]
        
        if (turn == 1):
                return max(minmax(indx * 2, curr_depth + 1, turn ^ 1, arr, target_depth), minmax(indx * 2 + 1, curr_depth + 1, turn ^ 1, arr, target_depth))
        else:
                return min(minmax(indx * 2, curr_depth + 1, turn ^ 1, arr, target_depth), minmax(indx * 2 + 1, curr_depth + 1, turn ^ 1, arr, target_depth))

def solve():
        # n = int(input("Enter Size: "))
        # arr = [0 for _ in range(n)]
        # for i in range(0, n):
        #         arr[i] = int(input())

        n = 8
        arr = [3, 5, 2, 9, 12, 5, 23, 23]
        
        for i in range(0, n):
                print(arr[i], end=" ")
        print()

        depth = int(math.log(len(arr), 2))

        print(depth)
        print("Total Optimal Value: ", minmax(0, 0, 1, arr, depth))
        print("Node Evaluate: ", node_evaluate)


if __name__ == '__main__':
        solve()