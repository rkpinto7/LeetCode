class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numsAsMap = {}
        ans = set()
        for i in range(len(nums)):
            target = -nums[i]
            for j in range(i+1, len(nums)):
                if(i!=j and (target - nums[j]) in numsAsMap):
                    
                    if(j != numsAsMap[target - nums[j]] and numsAsMap[target - nums[j]] != i):
                        triplet = [nums[i], nums[j], target - nums[j]]
                        triplet.sort()
                        #print(i, triplet)
                        ans.add(tuple(triplet))
                else:
                    numsAsMap[nums[j]] = j
        return list(ans)              
               
            
    
                    
                