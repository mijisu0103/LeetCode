class Solution:
  def threeSum(self, nums: list[int]) -> list[list[int]]:
    if len(nums) < 3:
      return []

    result = []

    nums.sort()

    for i in range(len(nums) - 2):
      if i > 0 and nums[i] == nums[i - 1]:
        continue

      left_start = i + 1
      right_start = len(nums) - 1

      while left_start < right_start:
        numssum = nums[i] + nums[left_start] + nums[right_start]
        if numssum == 0:
          result.append((nums[i], nums[left_start], nums[right_start]))
          left_start += 1
          right_start -= 1
          while nums[left_start] == nums[left_start - 1] and left_start < right_start:
            left_start += 1
          while nums[right_start] == nums[right_start + 1] and left_start < right_start:
            right_start -= 1
        elif numssum < 0:
          left_start += 1
        else:
          right_start -= 1

    return result