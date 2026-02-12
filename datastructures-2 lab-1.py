class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def _dfs(self, node, prefix, results):
        if node.is_end_of_word:
            results.append(prefix)

        for char, child in node.children.items():
            self._dfs(child, prefix + char, results)

    def autocomplete(self, prefix):
        node = self.root


        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        results = []
        self._dfs(node, prefix, results)
        return results



def main():
    trie = Trie()

    words = [
        "hello", "help", "helmet", "helicopter",
        "hero", "her", "heat", "heavy",
        "apple", "application", "apply"
    ]

    for word in words:
        trie.insert(word)

    print("Google Docs Autocomplete Simulation")
    print("Type something (type 'exit' to stop)\n")

    while True:
        prefix = input("You type: ").strip().lower()

        if prefix == "exit":
            print(" Exiting autocomplete")
            break

        suggestions = trie.autocomplete(prefix)

        if suggestions:
            print("Suggestions:", suggestions)
        else:
            print("No suggestions found")



if __name__ == "__main__":
    main()