class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level=0
        p=self.parent
        while p :
            level+=1
            p=p.parent

        return level

    def print_tree(self):
        spaces = " " *  self.get_level() * 3
        prefixes = spaces + "|--" if self.parent else " "
        print(prefixes + self.data)
        for child in self.children:
            child.print_tree()




def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Max"))
    laptop.add_child(TreeNode("Acer"))
    laptop.add_child(TreeNode("Victus"))

    phone = TreeNode("Phone")
    phone.add_child(TreeNode("redmi"))
    phone.add_child(TreeNode("iPhone"))
    phone.add_child(TreeNode("motorala"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(phone)
    root.add_child(tv)



    return root


if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree()
    # print(root.get_level())
    pass
