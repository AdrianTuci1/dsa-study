# Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Implement the WordDictionary class:

# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
# Constraints:

# 1 <= word.length <= 25
# word in addWord consists of lowercase English letters.
# word in search consist of '.' or lowercase English letters.
# There will be at most 2 dots in word for search queries.
# At most 
#  calls will be made to addWord and search.
# Probelm Explanation:
# The problem is to design a data structure called WordDictionary that allows you to add words and search for words efficiently. The key feature of this data structure is that it should support wildcard search, where a dot ('.') can match any letter.

# Here are the specific requirements and explanations for the problem:

# Initialize the WordDictionary object using the constructor WordDictionary().

# The addWord(word) method allows you to add a word to the data structure. Once added, you should be able to search for this word later. The words consist of lowercase English letters, and each word has a length between 1 and 25 characters.

# The search(word) method allows you to search for a word in the data structure. This method returns True if there is any string in the data structure that matches the given word or False otherwise. The word you are searching for may contain dots ('.'), where each dot can match any letter.

# The wildcard character ('.') in the search method allows for partial or fuzzy searching. For example, if the word dictionary contains the words "bad," "dad," and "mad," then:

# Searching for "pad" should return False because there is no exact match.
# Searching for "bad" should return True because "bad" is in the dictionary.
# Searching for ".ad" should return True because it can match "bad," "dad," or "mad."
# Searching for "b.." should return True because it can match "bad," "bed," "bet," etc.
# The problem specifies that there will be at most two dots ('.') in search queries, and there will be at most 10^4 calls to both addWord and search.

# In summary, you need to implement the WordDictionary class that efficiently supports adding words and searching for words, where the search can include wildcard characters ('.') that match any letter.

# # 


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            
            node = node.childre[char]

        node.is_end_of_word = True
    
    def searh_helper(self, node: TrieNode, word: str) -> bool:
        if not word:
            return node.is_end_of_word

        char = word[0]
        if char == '.':
            for child in node.children.values():
                if self.search_helper(child, word[1:]):
                    return True
        elif char in node.children:
            return self.search_helper(node.children[char], word[1:])

        return False
    
    def search(self, word: str) -> bool:
        return self.search_helper(self.root, word)

    

# Example 1: 

# Example usage:

wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("pad"))  # Output: False
print(wordDictionary.search("bad"))  # Output: True
print(wordDictionary.search(".ad"))  # Output: True
print(wordDictionary.search("b.."))  # Output: True
# False
# True
# True
# True