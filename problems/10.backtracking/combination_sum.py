# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to the target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

def combinationSum(candidates, target):
    def dfs(remaining, start, path):
        if remaining == 0:
            result.append(path)
            return

        if remaining < 0:
            return
        
        for i in range(start, len(candidates)):
            dfs(remaining - candidates[i], i, path + [candidates[i]])
    
    result = []
    candidates.sort()
    dfs(target, 0, [])
    return result

# Example 1: 

# Example 1
candidates1 = [2, 3, 6, 7]
target1 = 7
print(combinationSum(candidates1, target1))  # Output: [[2, 2, 3], [7]]
# [[2, 2, 3], [7]]