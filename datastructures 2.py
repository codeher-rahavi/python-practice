class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_end = True

    def _dfs(self, node, prefix, results):
        if node.is_end:
            results.append(prefix)
        for ch, child in node.children.items():
            self._dfs(child, prefix + ch, results)

    def autocomplete(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]

        results = []
        self._dfs(node, prefix, results)
        return results



trie = Trie()


words = [
    "array", "algorithm", "application", "api", "async",
    "binary", "backend", "bug", "boolean",
    "class", "compiler", "code", "cloud",
    "data", "database", "debug", "deploy",
    "function", "framework", "frontend"
]
for word in words:
    trie.insert(word)

print("Autocomplete System (type 'exit' to stop)")

while True:
    user_input = input("\nType something: ")

    if user_input.lower() == "exit":

        break

    suggestions = trie.autocomplete(user_input)

    if suggestions:
        print("Suggestions:", suggestions[:5])
    else:
        print("No suggestions found")