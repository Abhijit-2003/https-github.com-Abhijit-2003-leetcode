class Solution:
    def beautySum(self, s: str) -> int:
        total = 0

        for i in range(len(s)):
            freq = [0] * 26

            for j in range(i, len(s)):
                freq[ord(s[j]) - ord('a')] += 1

                max_freq = 0
                min_freq = float('inf')

                for count in freq:
                    if count > 0:
                        max_freq = max(max_freq, count)
                        min_freq = min(min_freq, count)

                total += max_freq - min_freq

        return total