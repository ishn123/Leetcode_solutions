class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        se = 0
        for i in nums:
            if i & 1 == 0:
                se += i
                
        ans = []     
        for q in queries:
            val = q[0]
            idx = q[1]
            
            if nums[idx] & 1 == 0:
                se -= nums[idx]
                if nums[idx] + val & 1 == 0:
                    se += nums[idx] + val
                    
                nums[idx] += val
            else:
                if nums[idx] + val & 1 == 0:
                    se += nums[idx] + val
                    
                nums[idx] += val
                
            ans.append(se)
            
        return ans