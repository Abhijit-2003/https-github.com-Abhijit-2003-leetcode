class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s.lower()
        t.lower()

        return ''.join(sorted(s)) == ''.join(sorted(t))