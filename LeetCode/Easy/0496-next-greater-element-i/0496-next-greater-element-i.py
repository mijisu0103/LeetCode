class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        hashmap = {}

        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                hashmap[prev] = num
            stack.append(num)

        for num in stack:
            hashmap[num] = -1

        return [hashmap[num] for num in nums1]