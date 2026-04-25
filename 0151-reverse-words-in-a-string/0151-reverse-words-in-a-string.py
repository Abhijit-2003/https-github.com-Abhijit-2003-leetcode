class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        stack = []

        i = 0
        while i < len(s):
            temp = ""
            while i < len(s) and s[i] != " ":
                temp += s[i]
                i += 1
            
            while i < len(s) and s[i] == " ":
                i += 1

            if len(temp) : stack.append(temp)

        stack.reverse()

        return " ".join(stack)