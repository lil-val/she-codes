class TreeNode:
    """A binary search tree relies on the property that keys that are less than the parent are found in the left subtree,
    and keys that are greater than the parent are found in the right subtree."""
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def print_tree(self):
        # print tree content
        if self.left_child:
            self.left_child.print_tree()
        print(self.value,)
        if self.right_child:
            self.right_child.print_tree()

    def insert(self, value):
        # insert new node with value
        if self.value:
            if value < self.value:
                if self.left_child is None:
                    self.left_child = TreeNode(value)
                else:
                    self.left_child.insert(value)
            elif value > self.value:
                if self.right_child is None:
                    self.right_child = TreeNode(value)
                else:
                    self.right_child.insert(value)
        else:
            self.value = value

    def lookup(self, value, parent=None):
        # lookup node containing data, returns node and node's parent if found or None, None
        if value < self.value:
            if self.left_child is None:
                return None, None
            return self.left_child.lookup(value, self)
        elif value > self.value:
            if self.right_child is None:
                return None, None
            return self.right_child.lookup(value, self)
        else:
            return self, parent

    def __str__(self):
        return str(self.value)

    def children_count(self):
        # return the number of children
        count = 0
        if self.left_child:
            count += 1
        if self.right_child:
            count += 1
        return count

    def delete(self, value, original_parent=None):
        # delete node containing value
        (current, parent) = self.lookup(value)
        if parent is None:
            parent = original_parent
        count = current.children_count()
        if parent:
            if count == 0:
                if parent.left_child == current:
                    parent.left_child = None
                elif parent.right_child == current:
                    parent.right_child = None
            elif count == 1:
                if current.left_child:
                    child = current.left_child
                else:
                    child = current.right_child
                if parent.left_child == current:
                    parent.left_child = child
                elif parent.right_child == current:
                    parent.right_child = child
            else:
                current.value = current.right_child.value
                current.right_child.delete(current.right_child.value, current)
        else:
            if count == 0:
                current.value = None
            elif count == 1:
                if current.left_child:
                    child = current.left_child
                else:
                    child = current.right_child
                current.value = child.value
                child.delete(child.value)
            else:
                current.value = current.right_child.value
                current.right_child.delete(current.right_child.value, current)


root = TreeNode(8)
root.insert(3)
root.insert(10)
root.insert(1)
root.insert(6)
root.insert(4)
root.insert(7)
root.insert(14)
root.insert(13)
lookup = root.lookup(6)
print(lookup[0], lookup[1])
root.print_tree()
root.delete(14)
root.print_tree()
