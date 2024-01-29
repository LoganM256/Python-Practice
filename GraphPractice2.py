class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self,treelvl):
        if self.get_level() > treelvl:
            return
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(treelvl)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_location_tree():
    # Gujarat Higherarchy
    guj = TreeNode("Gujarat")
    guj.add_child(TreeNode("Ahmedabad"))
    guj.add_child(TreeNode("Baroda"))

    #Karnataka Hierarchy
    kar = TreeNode("Karnataka")
    kar.add_child(TreeNode("Bangluru"))
    kar.add_child(TreeNode("Mysore"))

    #New Jersey Hierarchy
    nj = TreeNode("New Jersey")
    nj.add_child(TreeNode("Princeton"))
    nj.add_child(TreeNode("Trenton"))

    #California Hierarchy
    cal = TreeNode("California")
    cal.add_child(TreeNode("San Francisco"))
    cal.add_child(TreeNode("Mountain View"))
    cal.add_child(TreeNode("Palo Alto"))

    ind = TreeNode("India")
    ind.add_child(guj)
    ind.add_child(kar)

    usa = TreeNode("USA")
    usa.add_child(nj)
    usa.add_child(cal)

    glob = TreeNode("Global")
    glob.add_child(usa)
    glob.add_child(ind)

    return glob

if __name__ == "__main__":
    root_node = build_location_tree()
    root_node.print_tree(3)
    