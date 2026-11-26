# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
# Constraints:

# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 
#  calls in total will be made to insert, search, and startsWith.
# Probelm Explanation:
# The problem at hand is to implement a data structure known as a Trie (pronounced "try") or Prefix Tree. A Trie is a tree-like data structure that is used to efficiently store and retrieve a set of strings or words. It's particularly useful for tasks involving string manipulation, such as autocomplete and spell-checking. The problem statement defines the following operations for implementing the Trie class:

# Trie(): This is the constructor that initializes the Trie object.

# void insert(String word): This method inserts the given string word into the Trie. It effectively adds the characters of the word to the Trie's structure, creating nodes for each character if they don't already exist. At the end of the word, a special flag is set to indicate that this node represents the end of a valid word.

# boolean search(String word): This method checks if the given string word is present in the Trie. It starts from the root of the Trie and traverses the Trie by following the characters in the word. If it successfully traverses the Trie and reaches the end of the word, it returns true, indicating that the word exists in the Trie; otherwise, it returns false.

# boolean startsWith(String prefix): This method checks if there is any previously inserted word in the Trie that has the given prefix. It's similar to the search method but does not require that the prefix be a complete word. If there is any word in the Trie that starts with the given prefix, it returns true; otherwise, it returns false.

# The problem also provides an example scenario where these operations are called, demonstrating the expected output for each operation.

# In summary, the goal is to create a data structure (Trie) that efficiently stores a set of strings and provides methods to insert new strings, search for complete words, and check if a given prefix exists in the stored set of strings.


class TrieNode:
    def __init__(self):
        self.children = {} # dict to store child nodes
        self.is_end_of_word = False # indicates if a word ends at this node

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_end_of_word = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.is_end_of_word

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True



# Example 1: 

# Example usage:

trie = Trie()
trie.insert("apple")
print(trie.search("apple"))   # Output: True
print(trie.search("app"))     # Output: False
print(trie.startsWith("app")) # Output: True
trie.insert("app")
print(trie.search("app"))     # Output: True
# True
# False
# True
# True