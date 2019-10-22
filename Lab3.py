from RBTree import RBTreeNode
from RBTree import RBTree
from AVLTree import AVLTree
from AVLTree import Node

def create_avl(words):
        # create an avl tree
        avl_tree = AVLTree()
        # read the file
        file = open(words, "r")
        line = file.readline()
        # while loop to read all lines in file
        while line:
            # each word is added to the tree
            new_word = Node(line.rstrip().lower())
            avl_tree.AVL_Tree_Insert(new_word)
            line = file.readline()
        # return the tree
        return avl_tree


def number_anagrams(word, tree):
    # creates a list of words
    permutations = tree.print_anagrams(word)
    # set count to 0
    count = 0
    # traverse the list
    for i in range(len(permutations)):
        if tree.search(permutations[i]):
            count += 1

    return count

def create_rb(words):
        # create an rb tree
        rb_tree = RBTree()
        # read the file
        file = open(words, "r")
        line = file.readline()
        # while loop to read all lines in file
        while line:
            # each word is added to the tree
            new_word = Node(line.rstrip().lower())
            rb_tree.insert(new_word)
            line = file.readline()
        # return the tree
        return rb_tree

def main():
    print("What kind of tree do you want?")
    print("Type the number.")
    kind_of_tree = input("1. Red Black Tree\n2. AVL Tree\n")
    if kind_of_tree == '1':
        rb_tree = create_rb("words.txt")
        rb_tree.print_anagrams("step")
    elif kind_of_tree == '2':
        AVL_Tree = create_avl("words2.txt")
        AVLTree.print_anagrams('step',"")

    

if __name__=="__main__":
    main()