class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        n = len(num_str)
        last_occurrence = {}
        
        for i in range(n):
            last_occurrence[num_str[i]] = i

        for i in range(n):
            for d in range(9, int(num_str[i]), -1):
                d_str = str(d)
                if d_str in last_occurrence and last_occurrence[d_str] > i:
                    num_str[i], num_str[last_occurrence[d_str]] = num_str[last_occurrence[d_str]], num_str[i]
                    return int("".join(num_str))
        return num