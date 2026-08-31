class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children =[]
        self.parent =None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def getlevel(self):
        level = 0
        i=self.parent
        while i:
            level +=1
            i = i.parent

        return level


    def print_root(self):
        spaces = self.getlevel()
        print(spaces+self.data)
        if self.children:
            for child in self.children:
                child.print_root()

#create the root tree with the help of the treeNode and the append children function
def build_Tree():
    root= TreeNode('Electronics')

    laptop = TreeNode('Laptop')
    laptop.add_child(TreeNode('Apple'))
    laptop.add_child(TreeNode('Acer'))
    laptop.add_child(TreeNode('Dell'))

    phone = TreeNode('Phones')
    phone.add_child(TreeNode('Redmi'))
    phone.add_child(TreeNode('Realme'))
    phone.add_child(TreeNode('lenova'))

    watch = TreeNode('Watches')
    watch.add_child(TreeNode('Sonata'))
    watch.add_child(TreeNode('Casio'))

    root.add_child(laptop)
    root.add_child(phone)
    root.add_child(watch)

    return root

if __name__ == "__main__":
    root = build_Tree()
    root.print_root()






