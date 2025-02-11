class Trie_Node:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root  = Trie_Node()

    def insert(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Trie_Node()
            node = node.children[char]
        print(f'{word} inserted successfully.')
        node.isEndOfWord = True

    def search(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def startsWith(self,prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def delete(self,word):
        def _delete(node,word,depth):
            if not node:
                return False
            if depth == len(word):
                if not node.isEndOfWord:
                    return False
                node.isEndOfWord = False
                return len(node.children)==0
            
            char = word[depth]
            if char not in node.children:
                return False
            
            make_delete = _delete(node.children[char],word,depth+1)

            if make_delete:
                del node.children[char]
                return len(node.children)==0
            return False
        
        _delete(self.root,word,0)


    def getwordsWithPrefix(self,prefix):
        def dfs(node,prefix,results):
            if node.isEndOfWord:
                results.append(prefix)
            
            for char,child in node.children.items():
                dfs(child,prefix+char,results)

        node = self.root
        results = []

        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        
        dfs(node,prefix,results)
        return results




trie = Trie()

trie.insert('hello')
trie.insert('hai')
trie.insert('hellow')

print(trie.search('hello'))
print(trie.startsWith('hai'))

trie.delete('hello')
print(trie.search('hello'))
trie.insert('flower')
trie.insert('fley')
trie.insert('pen')

print(trie.startsWith('he'))
print(trie.getwordsWithPrefix('p'))