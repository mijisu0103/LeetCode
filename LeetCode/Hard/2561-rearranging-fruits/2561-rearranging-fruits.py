class Solution:
  def minCost(self, basket1: list[int], basket2: list[int]) -> int:
    
    swapped = []
    count = collections.Counter(basket1)
    count.subtract(collections.Counter(basket2))

    for num, freq in count.items():
      if freq % 2 != 0:
        return -1
      swapped += [num] * abs(freq // 2)

    swapped.sort()
    minNum = min(min(basket1), min(basket2))
    return sum(min(2 * minNum, num) for num in swapped[0:len(swapped) // 2])

