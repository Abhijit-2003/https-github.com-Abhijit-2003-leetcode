class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s) % 2) != 0 : return False

        paren = {'(':')','[':']','{':'}'}
        stack = []
        for ch in s :
            if ch in ['(', '[', '{'] :
                stack.append(ch)
            
            if ch in [')', ']', '}'] :
                if len(stack) == 0 : return False
                temp = stack.pop()
                if ch != paren.get(temp):
                    return False
                
        return len(stack) == 0