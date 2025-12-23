import math

node_evaluate = 0
cnt = []

def alpha_beta_prunning(indx, curr_depth, turn, arr, target_depth, alpha, beta):
        global node_evaluate, cnt
        node_evaluate += 1
        
        if (curr_depth == target_depth):
                # node_evaluate += 1  # Only count when we reach a leaf node
                return arr[indx]
        
        if (turn == 1): # maximum...
                best = -math.inf
                for i in range(2):
                        val = alpha_beta_prunning(indx * 2 + i, curr_depth + 1, turn ^ 1, arr, target_depth, alpha, beta)
                        best = max(val, best)
                        alpha = max(alpha, best)
                        if (alpha >= beta): # cut-off
                                return best
                return best
        else: # minimum...
                best = math.inf
                for i in range(2):
                        val = alpha_beta_prunning(indx * 2 + i, curr_depth + 1, turn ^ 1, arr, target_depth, alpha, beta)
                        best = min(best, val)
                        beta = min(beta, best)
                        if (alpha >= beta):
                                return best
                return best

def minmax(indx, curr_depth, turn, arr, target_depth):
        # print()
        global node_evaluate, cnt
        node_evaluate += 1

        if (curr_depth == target_depth):
                return arr[indx]
        
        if (turn == 1):
                return max(minmax(indx * 2, curr_depth + 1, turn ^ 1, arr, target_depth), minmax(indx * 2 + 1, curr_depth + 1, turn ^ 1, arr, target_depth))
        else:
                return min(minmax(indx * 2, curr_depth + 1, turn ^ 1, arr, target_depth), minmax(indx * 2 + 1, curr_depth + 1, turn ^ 1, arr, target_depth))



def solve():
        global node_evaluate, cnt
        # n = int(input("Enter Size: "))
        # arr = [0 for _ in range(n)]
        # for i in range(0, n):
        #         arr[i] = int(input())

        n = 8
        arr = [3, 5, 2, 9, 12, 5, 23, 23]
        cnt = [0] * 4 * n

        for i in range(0, n):
                print(arr[i], end=" ")
        print()

        depth = int(math.log(len(arr), 2))

        print(depth)
        print("Optimal Value: ", minmax(0, 0, 1, arr, depth))
        print("Node Evaluate: ", node_evaluate)

        # Alpha-Beta Prunning....
        node_evaluate = 0

        print("\nUsing Alpha-Beta-Prunning")
        print("Optimal Value: ", alpha_beta_prunning(0, 0, 1, arr, depth, -math.inf, math.inf)) # alpha = maximum, beta = minimum...
        print("Node Evaluate: ", node_evaluate)

if __name__ == '__main__':
        solve()