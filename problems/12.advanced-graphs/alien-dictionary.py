# There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

# Constraints:

# You may assume all letters are in lowercase.
# The dictionary is invalid, if string a is prefix of string b and b is appear before a.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return the smallest in normal lexicographical order.
# The letters in one string are of the same rank by default and are sorted in Human dictionary order.

from collections import defaultdict, deque

def alienOrder(words):
    #create an adjacency list to represent the graph
    graph = defaultdict(list)

    #create a dictionary to store the in-degrees of each letter
    in_degree = {}

    #initialize in-degrees to 0 for all letters
    for word in words:
        for char in word:
            if char not in in_degree:
                in_degree[char] = 0
    
    #build the graph and unpdate in-degrees
    for i in range(1, len(words)):
        word1, word2 = words[i - 1], words[i]
        min_length = min(len(word1), len(word2))

        #compare characters in the two words
        j = 0
        while j < min_length and word1[j] == word2[j]:
            j += 1

        if j < min_length:
            #if word1[j] is lexicographically before word2[j], add an edge
            graph[word1[j]].append(word2[j])
            in_degree[word2[j]] += 1

            #break the loop to avoid further comparisons
            break
    
    #perform topological sorting using kahn's alghorithm
    result = []
    queue = deque([char for char in in_degree if in_deegree[char] == 0])

    while queue:
        char = queue.popleft()
        result.append(char)

        for neighbor in graph[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    #check if there is a valid order
    if len(result) < len(in_degree):
        return ""
    
    return "".join(result)


# Example 1
words1 = ["wrt", "wrf", "er", "ett", "rftt"]
print(alienOrder(words1))  
# Output: "wertf"

