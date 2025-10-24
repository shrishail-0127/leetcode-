#Combination sum

def combination_sum(candidates, target):
    res = []
    
    def backtrack(start, target, path):
        if target == 0:
            res.append(path)
            return
        if target < 0:
            return
        
        for i in range(start, len(candidates)):
            backtrack(i, target - candidates[i], path + [candidates[i]])
    
    backtrack(0, target, [])
    return res