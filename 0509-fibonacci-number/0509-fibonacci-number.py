class Solution:
    def helper(self, n) :
        if n == 0 or n == 1 :
            return n

        return self.helper(n-1) + self.helper(n-2)

    def fib(self, n: int) -> int :
        return self.helper(n)
        