class Solution:
  def threeSumClosest(self, nums: list[int], target: int) -> int:
    result = nums[0] + nums[1] + nums[2]

    nums.sort()

    for i in range(len(nums) - 2):
      if i > 0 and nums[i] == nums[i - 1]:
        continue

      left = i + 1
      right = len(nums) - 1
      while left < right:
        tsum = nums[i] + nums[left] + nums[right]
        if tsum == target:
          return tsum
        if abs(tsum - target) < abs(result - target):
          result = tsum
        if tsum < target:
          left += 1
        else:
          right -= 1

    return result