class TrieNode:
    def __init__(self):
        self.children = {}
        self.endNode = False   #indicates if it is end of the word)
        
class Trie:

    def __init__(self):
        self.root = TrieNode()       

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:     # create new node
                cur.children[c] = TrieNode()
            cur = cur.children[c]   # cur pointer moves to the current char
        cur.endNode = True          # at the end of the word cur pointer points to last char so set cur.endNode to True (all the oother nodes will have endNode attributes set to default which is false except this one)
        

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        # check if it is exect word
        if cur.endNode == True:
            return True
        else:
            return False

#    used in autocomplete
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)