class Node:
    def __init__(self, key, parent = None, left = None, right = None, height = 0):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        self.height = height
    
    def AVL_Tree_Update_Height(self):
        leftHeight = -1
        if self.left is not None:
            leftHeight = self.left.height
        rightHeight = -1
        if self.right is not None:
            rightHeight = self.right.height
        self.height = max(leftHeight, rightHeight) + 1

    def AVL_Tree_Get_Balance(self): 
        leftHeight = -1
        if self.left is not None:
            leftHeight = self.left.height
        rightHeight = -1
        if self.right is not None:
            rightHeight = self.right.height
        return leftHeight - rightHeight

    def AVL_Tree_Set_Child(self, whichChild, child):
        if whichChild != "left" and whichChild != "right":
            return False

        if whichChild == "left":
            self.left = child
        else:
            self.right = child
        if child is not None:
            child.parent = self

        parent.AVL_Tree_Update_Height()
        return True

    def AVL_Tree_Replace_Child(self, currentChild, newChild):
        if self.left is currentChild:
            return self.AVL_Tree_Set_Child("left", newChild)
        elif self.right is currentChild:
            return parent.AVL_Tree_Set_Child("right", newChild)
        return False

class AVLTree:
    def __init__(self,root=None):
        self.root = root

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
    
    def AVL_Tree_Insert(self, node):
        if self.root is None:
            self.root = node
            node.parent = None
            return
   
        cur = self.root
        while cur is not None:
            if node.key < cur.key:
                if cur.left is None:
                    cur.left = node
                    node.parent = cur
                    cur = None
                else:
                    cur = cur.left
            else:
                if cur.right is None: 
                    cur.right = node
                    node.parent = cur
                    cur = None
                else:
                    cur = cur.right
      
        node = node.parent
        while node is not None: 
            self.AVL_Tree_Rebalance(node)
            node = node.parent
    
    def AVL_Tree_Rebalance(self, node):
        node.AVL_Tree_Update_Height()        
        if node.AVL_Tree_Get_Balance == -2: 
            if node.right.AVL_Tree_Get_Balance == 1:
            #Double rotation case.
                AVL_Tree_Rotate_Right(self, node.right)
            return AVL_Tree_Rotate_Left(self, node)
        elif node.AVL_Tree_Get_Balance == 2:
            if node.left.AVL_Tree_Get_Balance == -1:
                #Double rotation case.
                AVL_Tree_Rotate_Left(self, node.left)
            return AVL_Tree_Rotate_Right(self, node)       
        return node

    def AVL_Tree_Rotate_Right(self, node):
        rightLeftChild = node.right.left
        if node.parent is not None:
            node.parent.AVL_Tree_Replace_Child(node, node.right)
        else: # node is root
            self.root = node.right
            self.root.parent = None
   
        node.left.AVL_Tree_Set_Child("left", node)
        node.AVL_Tree_Set_Child("right", rightLeftChild)

    def AVL_Tree_Rotate_Left(self, node):
        leftRightChild = node.left.right
        if node.parent is not None:
            node.parent.AVL_Tree_Replace_Child(node, node.left)
        else: # node is root
            self.root = node.left
            self.root.parent = None
   
        node.left.AVL_Tree_Set_Child("right", node)
        node.AVL_Tree_Set_Child("left", leftRightChild)

    