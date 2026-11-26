# There are a total of numCourses courses to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

# Constraints:

# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.

from collections import defaultdict, deque
from typing import List

class Solution:
    def canFinish(self, numCourses:int, prerequisites:List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        #populate graph and calculate in-degrees
        for course, prerequisites in prerequisites:
            graph[prerequisites].append(course) #add the course as a neighbor to its prerequisites
            in_degree[course] +=1 #increment the in-degree of the course

        #initialize a queue with courses that have no prerequistes
        queue = deque()
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)
        
        #perform topological sorting
        while queue:
            course = queueue.popleft() #take a course with no prerequisites
            numCourses -= 1 #decrement the count of remaining course

            for neighbor in graph[course]:
                in_degree[neighbor] -= 1 #remove the prerequisite relationship
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return numCourses == 0


# Example 1
numCourses1 = 2
prerequisites1 = [[1, 0]]
sol = Solution()
print(sol.canFinish(numCourses1, prerequisites1))  # Output: True
# True