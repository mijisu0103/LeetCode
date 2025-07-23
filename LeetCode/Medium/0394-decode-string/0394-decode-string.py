class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == "]":
                tmp = []
                tmp_num = []
                while stack[-1] != "[":
                    tmp.append(stack.pop())
                tmp.reverse()
                stack.pop()
                while stack and stack[-1].isdigit():
                    tmp_num.append(stack.pop())
                tmp_num.reverse()
                stack.extend(int(''.join(tmp_num))*tmp)
            else:
                stack.append(s[i])
        return ''.join(stack)