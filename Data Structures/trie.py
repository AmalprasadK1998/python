


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # inserting words into a trie
    def insert(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.end_of_word = True

    # searching for a word in a trie
    def search(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.end_of_word


    # finding all words with a given prefix in trie
    def starts_with(self, prefix):
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return []
            current_node = current_node.children[char]
        return self._dfs(current_node, prefix)

    def _dfs(self, node, prefix):
        words = []
        if node.end_of_word:
            words.append(prefix)
        for char, child_node in node.children.items():
            words.extend(self._dfs(child_node, prefix + char))
        return words

trie = Trie()
trie.insert("hello")
trie.insert("world")
trie.insert("help")
trie.insert("he")

print(trie.search("hello")) # True
print(trie.search("world")) # True
print(trie.search("foo")) # False




print(trie.starts_with("he")) # ['hello', 'help', 'he']
print(trie.starts_with("w")) # ['world']
print(trie.starts_with("foo")) # []





