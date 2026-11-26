# Problem Statement
# Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

# Example 1:

# Intervals: [[1,4], [2,5], [7,9]]
# Output: [[1,5], [7,9]]
# Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into one [1,5].


def print_interval(i):
    print("[" + str(i.start) + ", " + str(i.end) + "]", end='')


class Solution:
    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals
        intervals.sort(key=lambda x: x.start)
        mergedIntervals = []
        start = intervals[0].start
        end = intervals[0].end
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval.start <= end:
                end = max(interval.end, end)
            else:
                mergedIntervals.append(Interval(start, end))
                start = interval.start
                end = interval.end
        mergedIntervals.append(Interval(start, end))
        return mergedIntervals

    
def main():
  sol = Solution()
  print("Merged intervals: ", end='')
  for i in sol.merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
    print_interval(i)
  print()

  print("Merged intervals: ", end='')
  for i in sol.merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
    print_interval(i)
  print()

  print("Merged intervals: ", end='')
  for i in sol.merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
    print_interval(i)
  print()


main()