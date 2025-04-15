class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN=-(2**31)
        INT_MAX=(2**31)-1
        
        s=s.strip()
        
        first=None
        for c in s:
            if not first:
                if c.isdigit() or c in {'-','+'}: 
                    first=c 
                else:
                    break
            else: 
                if c.isdigit():
                    first+=c
                else:
                    break
        
        if not first or first in {'-','+'}:
            first=0
        elif int(first)<INT_MIN:
            first=INT_MIN
        elif int(first)>INT_MAX:
            first=INT_MAX
            
        return int(first)