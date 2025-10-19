class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def findLeft():
            l, r = 0, len(nums) - 1
            index = -1
            
            while l <= r:
                mid = (l + r) // 2
                
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
                if nums[mid] == target:
                    index = mid
            
            return index

        def findRight():
            l, r = 0, len(nums) - 1
            index = -1
            
            while l <= r:
                mid = (l + r) // 2
                
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
                if nums[mid] == target:
                    index = mid
            
            return index

        left = findLeft()
        right = findRight()

        return [left, right]