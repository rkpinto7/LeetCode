class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        hash_set = set()
        return_list = []

        def backtracker(curr_arr, curr_sum):
            if curr_sum > target:
                return
            if curr_sum == target:
                curr_arr.sort()
                if tuple(curr_arr) not in hash_set:
                    hash_set.add(tuple(curr_arr))
                    return_list.append(curr_arr[:])  # Use 
            else:
                for num in candidates:
                    if curr_sum + num <= target:
                        curr_arr.append(num)
                        backtracker(curr_arr[:], curr_sum + num)
                        curr_arr.pop()
                    else:
                        break

        backtracker([], 0)
        return return_list
