class Solution:
    def equalFrequency(self, word: str) -> bool:
        hashCounter = {}

        for char in word:
            hashCounter[char] = hashCounter.get(char, 0) + 1

        for key, value in hashCounter.items():
            hashCounter[key] -= 1
            tempSet = set()

            for val in hashCounter.values():
                if val > 0:
                    tempSet.add(val)

            if len(tempSet) == 1:
                return True
            
            hashCounter[key] += 1

        return False