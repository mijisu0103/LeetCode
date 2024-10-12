class Solution:
  def letterCombinations(self, digits: str) -> list[str]:
    if not digits:
      return []

    ToLetters = ['', '', 'abc', 'def', 'ghi',
                      'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    result = []

    def search(i: int, comb: list[str]) -> None:
      if i == len(digits):
        result.append(''.join(comb))
        return

      for letter in ToLetters[int(digits[i])]:
        comb.append(letter)
        search(i + 1, comb)
        comb.pop()

    search(0, [])
    return result