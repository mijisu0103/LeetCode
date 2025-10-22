class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        counts = []
        
        cur = None
        
        for i in range(0, len(s)):
            
            if not cur:
                cur = [s[i], 1]
                continue
            
            if s[i] == cur[0]:
                cur[1] += 1
                if cur[1] == k:
                    cur = counts.pop() if counts else None
            else:
                counts.append(cur)
                cur = [s[i], 1]
        
        if cur:
            counts.append(cur)
        return "".join(
            char * count for char, count in counts
        )