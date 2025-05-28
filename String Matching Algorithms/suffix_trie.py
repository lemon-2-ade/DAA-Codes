class SuffixTrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class SuffixTrie:
    def __init__(self, text: str):
        self.root = SuffixTrieNode()
        self.build_suffix_trie(text)
    
    def build_suffix_trie(self, text: str):
        for i in range(len(text)):
            current = self.root

            for j in range(i, len(text)):
                char = text[j]

                if char not in current.children:
                    current.children[char] = SuffixTrieNode()
                current = current.children[char]

            current.is_end = True

    def search(self, pattern: str) -> bool:
        current = self.root

        for char in pattern:
            if char not in current.children:
                return False
            current = current.children[char]
        
        return True

if __name__ == '__main__':
    text = 'banana'
    trie = SuffixTrie(text)

    print(trie.search('ana'))
    print(trie.search('ban'))
    print(trie.search('xyz'))