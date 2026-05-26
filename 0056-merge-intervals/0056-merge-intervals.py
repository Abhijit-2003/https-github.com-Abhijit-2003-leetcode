class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort intervals
        intervals.sort(key=lambda x: x[0])

        ans = []

        # Add first interval
        ans.append(intervals[0])

        # Step 2: Traverse remaining intervals
        for i in range(1, len(intervals)):

            current = intervals[i]
            last = ans[-1]

            # Overlap
            if current[0] <= last[1]:

                last[1] = max(last[1], current[1])

            # No overlap
            else:
                ans.append(current)

        return ans