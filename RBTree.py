class RBTreeNode:
    def __init__(self, key, parent, red=False, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

        if red:
            self.color = "red"
        else:
            self.color = "black"

    def red(self):
        return self.color == "red"

    def black(self):
        return self.color == "black"

    def RB_Tree_Get_Grandparent(self):
        if self.parent is None:
            return None
        return self.parent.parent

    def RB_Tree_Get_Sibling(self):
        if self.parent is not None:
            if self is self.parent.left:
                return self.parent.right
            return self.parent.left
        return None

    def size(self):
        counter = 1
        if self.left is not None:
            counter += self.left.size()
        if self.right is not None:
            counter += self.right.size()
        return counter

    def RB_Tree_Get_Uncle(self):
        grandparent = self.RB_Tree_Get_Grandparent()
        if grandparent is None:
            return None
        if grandparent.left is self.parent:
            return grandparent.right
        else:
            return grandparent.left

    # Sets either the left or right child of this node
    def RB_Tree_Set_Child(self, whichChild, child):
        if whichChild != "left" and whichChild != "right":
            return False
        if whichChild == "left":
            self.left = child
        else:
            self.right = child
        if child is not None:
            child.parent = self
        return True

    def RB_Tree_Replace_Child(self, currentChild, newChild):
        if self.left is currentChild:
            return self.RB_Tree_Set_Child("left", newChild)
        elif self.right is currentChild:
            return self.RB_Tree_Set_Child("right", newChild)
        return False

    def RB_Tree_Are_Both_Children_Black(self):
        if self.left is not None and self.left.red():
            return False
        if self.right is not None and self.right.red():
            return False
        return True

    def RB_Tree_Get_Predecessor(self):
        node = self.left
        while node.right is not None:
            node = node.right
        return node

    


class RBTree:
    def _init_(self, root = None):
        self.root = root

    def RB_Tree_Length(self):
        if self.root is None:
            return 0
        return self.root.size()

    def print_anagrams(self,word, prefix=""):
        if len(word) <= 1:
            str2 = prefix + word

            if self.search(str2):
                print(prefix + word)
        else:
            for i in range(len(word)):
                cur = word[i: i + 1]
                before = word[0: i] # letters before cur
                after = word[i + 1:] # letters after cur

                if cur not in before: # Check if permutations of cur have not been generated.
                    print_anagrams(before + after, prefix + cur)

    def insert(self, key):
        new = RBTreeNode(key, None, True, None, None)
        self.insert_helper(new)

    def insert_helper(self, node):

        if self.root is None:
            self.root = node
        else:
            curr = self.root
            while curr is not None:
                if node.key < curr.key:
                    if curr.left is None:
                        curr.RB_Tree_Set_Child("left", node)
                        break
                    else:
                        curr = curr.left
                else:
                    if curr.right is None:
                        curr.RB_Tree_Set_Child("right", node)
                        break
                    else:
                        curr = curr.right

        node.color = "red"

        self.RB_Tree_Balance(node)

    def RB_Tree_Balance(self, node):
        # If node is root, set color black
        if node.parent is None:
            node.color = "black"
            return

        if node.parent.black():
            return

        parent = node.parent
        grandparent = node.RB_Tree_Get_Grandparent()
        uncle = node.RB_Tree_Get_Uncle()

        # change parent and uncle from red to black to color grandparent red
        if uncle is not None and uncle.red():
            parent.color = "black"
            uncle.color = "black"
            grandparent.color = "red"
            self.RB_Tree_Balance(grandparent)
            return

        # If node is parent's right and parent is grandparent's left, rotate left at parent
        if node is parent.right and parent is grandparent.left:
            self.RB_Tree_Rotate_Left(parent)
            node = parent
            parent = node.parent
        # If node is parent's left and parent is grandparent's right, rotate right at parent
        elif node is parent.left and parent is grandparent.right:
            self.RB_Tree_Rotate_Right(parent)
            node = parent
            parent = node.parent

        # change parent black and grandparent red
        parent.color = "black"
        grandparent.color = "red"

        # If node is parent's left child, then rotate right at grandparent, otherwise rotate left at grandparent
        if node is parent.left:
            self.RB_Tree_Rotate_Right(grandparent)
        else:
            self.RB_Tree_Rotate_Left(grandparent)

    def search(self, key):
        curr = self.root
        while curr is not None:
            if curr.key == key:
                return True
            elif curr.key < key:
                curr = curr.right
            else:
                curr = curr.left
        return False

    def RB_Tree_Rotate_Left(self, node):
        rightLeftChild = node.right.left
        if node.parent is not None:
            node.parent.RB_Tree_Replace_Child(node, node.right)
        else:  # node is root
            self.root = node.right
            self.root.parent = None
        node.right.RB_Tree_Set_Child("left", node)
        node.RB_Tree_Set_Child("right", rightLeftChild)

    def RB_Tree_Rotate_Right(self, node):
        leftRightChild = node.left.right
        if node.parent is not None:
            node.parent.RB_Tree_Replace_Child(node, node.left)
        else:  # node is root
            self.root = node.left
            self.root.parent = None
        node.left.RB_Tree_Set_Child("right", node)
        node.RB_Tree_Set_Child("left", leftRightChild)
