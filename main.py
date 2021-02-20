import binarysearchtree
import binarytree
import treechecker
import node

"""
main(): 
initializes binary search trees, binary trees and tree_checker
builds each binary search tree from a corresponding list of values
builds each binary tree by manually setting the root and children
traverses each tree in inorder, preorder, and postorder
compares each pair of trees to see if they are mirrors, identical, or neither
removes a given value from each tree, traverses, then compares again
"""
if __name__ == '__main__':
    # initializing lists, bsts, bin_trees, and tree_checker
    list1 = [4, 1, 9, 12, 3, 2, 8, 7, 16, 20, 13, 11]
    list2 = [4, 1, 9, 12, 3, 2, 8, 7, 16, 20, 13, 11]
    list3 = [3, 2, 6, 1, 5, 8, 4, 12, 10, 9, 19, 7]
    list4 = [5, 4, 2, 1, 6, 13, 8, 14, 12, 17, 18, 3]
    bst1 = binarysearchtree.BinarySearchTree()
    bst2 = binarysearchtree.BinarySearchTree()
    bst3 = binarysearchtree.BinarySearchTree()
    bst4 = binarysearchtree.BinarySearchTree()
    bin_tree1 = binarytree.BinaryTree()
    bin_tree2 = binarytree.BinaryTree()
    bin_tree3 = binarytree.BinaryTree()
    bin_tree4 = binarytree.BinaryTree()
    tree_checker = treechecker.TreeChecker()

    # building bst1
    for i in list1:
        root = getattr(bst1, "_BinarySearchTree__root")
        setattr(bst1, "_BinarySearchTree__root", bst1.insert(i))
    # traversing bst1
    print("\nBST1")
    print("Inorder Traversal:  ", end=" ")
    data_list1 = bst1.inorder()
    print("\nPreorder Traversal: ", end=" ")
    bst1.preorder()
    print("\nPostorder Traversal:", end=" ")
    bst1.postorder()
    print('\n')

    # building bst2
    for i in list2:
        root = getattr(bst2, "_BinarySearchTree__root")
        setattr(bst2, "_BinarySearchTree__root", bst2.insert(i))
    # traversing bst2
    print("BST2")
    print("Inorder Traversal:  ", end=" ")
    bst2.inorder()
    print("\nPreorder Traversal: ", end=" ")
    bst2.preorder()
    print("\nPostorder Traversal:", end=" ")
    bst2.postorder()
    print('\n')

    # comparing bst1 and bst2
    if tree_checker.is_mirror(getattr(bst1, "_BinarySearchTree__root"),
                              getattr(bst2, "_BinarySearchTree__root")):
        print("Binary Search Trees are mirrors of each other.")
    elif tree_checker.is_same(getattr(bst1, "_BinarySearchTree__root"),
                              getattr(bst2, "_BinarySearchTree__root")):
        print("Binary Search Trees are identical to each other.")
    else:
        print("Binary Search Trees are not related to each other.")

    # removing a random value from each tree
    if bst1.remove(4):
        print("Removed value 4 from BST1.")
    print("Inorder Traversal: ", end=" ")
    bst1.inorder()
    if bst2.remove(12):
        print("\nRemoved value 12 from BST2.")
    print("Inorder Traversal:", end=" ")
    bst2.inorder()

    # comparing bst1 and bst2 again
    if tree_checker.is_mirror(getattr(bst1, "_BinarySearchTree__root"),
                              getattr(bst2, "_BinarySearchTree__root")):
        print("\nBinary Search Trees are mirrors of each other.\n")
    elif tree_checker.is_same(getattr(bst1, "_BinarySearchTree__root"),
                              getattr(bst2, "_BinarySearchTree__root")):
        print("\nBinary Search Trees are identical to each other.\n")
    else:
        print("\nBinary Search Trees are not related to each other.\n")

    # building bst3
    for i in list3:
        root = getattr(bst3, "_BinarySearchTree__root")
        setattr(bst3, "_BinarySearchTree__root", bst3.insert(i))
    # traversing bst3
    print("\nBST3")
    print("Inorder Traversal:  ", end=" ")
    bst3.inorder()
    print("\nPreorder Traversal: ", end=" ")
    bst3.preorder()
    print("\nPostorder Traversal:", end=" ")
    bst3.postorder()
    print('\n')

    # building bst4
    for i in list4:
        root = getattr(bst4, "_BinarySearchTree__root")
        setattr(bst4, "_BinarySearchTree__root", bst4.insert(i))
    # traversing bst4
    print("BST4")
    print("Inorder Traversal:  ", end=" ")
    bst4.inorder()
    print("\nPreorder Traversal: ", end=" ")
    bst4.preorder()
    print("\nPostorder Traversal:", end=" ")
    bst4.postorder()
    print('\n')

    # comparing bst3 and bst4
    if tree_checker.is_mirror(getattr(bst3, "_BinarySearchTree__root"),
                              getattr(bst4, "_BinarySearchTree__root")):
        print("Binary Search Trees are mirrors of each other.")
    elif tree_checker.is_same(getattr(bst3, "_BinarySearchTree__root"),
                              getattr(bst4, "_BinarySearchTree__root")):
        print("Binary Search Trees are identical to each other.")
    else:
        print("Binary Search Trees are not related to each other.")

    # removing a random value from each tree
    if bst3.remove(1):
        print("Removed value 1 from BST3.")
    print("Inorder Traversal:", end=" ")
    bst3.inorder()
    if bst4.remove(2):
        print("\nRemoved value 16 from BST4.")
    print("Inorder Traversal:", end=" ")
    bst4.inorder()

    # comparing bst3 and bst4 again
    if tree_checker.is_mirror(getattr(bst3, "_BinarySearchTree__root"),
                              getattr(bst4, "_BinarySearchTree__root")):
        print("\nBinary Search Trees are mirrors of each other.\n")
    elif tree_checker.is_same(getattr(bst3, "_BinarySearchTree__root"),
                              getattr(bst4, "_BinarySearchTree__root")):
        print("\nBinary Search Trees are identical to each other.\n")
    else:
        print("\nBinary Search Trees are not related to each other.\n")

    # building bin_tree1
    setattr(bin_tree1, "_BinaryTree__root", node.Node())
    root = getattr(bin_tree1, "_BinaryTree__root")
    setattr(root, "_Node__data", 4)
    setattr(root, "_Node__left_child", node.Node())
    root_left_child = getattr(root, "_Node__left_child")
    setattr(root_left_child, "_Node__data", 3)
    setattr(root, "_Node__right_child", node.Node())
    root_right_child = getattr(root, "_Node__right_child")
    setattr(root_right_child, "_Node__data", 1)
    setattr(root_left_child, "_Node__left_child", node.Node())
    setattr(getattr(root_left_child, "_Node__left_child"), "_Node__data", 6)
    setattr(root_left_child, "_Node__right_child", node.Node())
    setattr(getattr(root_left_child, "_Node__right_child"), "_Node__data", 7)
    print("\nBinary Tree 1")
    print("Inorder Traversal:  ", end=" ")
    bin_tree1.inorder()
    print("\nPreorder Traversal: ", end=" ")
    bin_tree1.preorder()
    print("\nPostorder Traversal:", end=" ")
    bin_tree1.postorder()
    print('\n')

    # building bin_tree2
    setattr(bin_tree2, "_BinaryTree__root", node.Node())
    root = getattr(bin_tree2, "_BinaryTree__root")
    setattr(root, "_Node__data", 4)
    setattr(root, "_Node__left_child", node.Node())
    root_left_child = getattr(root, "_Node__left_child")
    setattr(root_left_child, "_Node__data", 1)
    setattr(root, "_Node__right_child", node.Node())
    root_right_child = getattr(root, "_Node__right_child")
    setattr(root_right_child, "_Node__data", 3)
    setattr(root_right_child, "_Node__left_child", node.Node())
    setattr(getattr(root_right_child, "_Node__left_child"), "_Node__data", 7)
    setattr(root_right_child, "_Node__right_child", node.Node())
    setattr(getattr(root_right_child, "_Node__right_child"), "_Node__data", 6)
    print("Binary Tree 2")
    print("Inorder Traversal:  ", end=" ")
    bin_tree2.inorder()
    print("\nPreorder Traversal: ", end=" ")
    bin_tree2.preorder()
    print("\nPostorder Traversal:", end=" ")
    bin_tree2.postorder()
    print('\n')

    # comparing bin_tree1 and bin_tree2
    if tree_checker.is_mirror(getattr(bin_tree1, "_BinaryTree__root"),
                              getattr(bin_tree2, "_BinaryTree__root")):
        print("Binary Trees are mirrors of each other.")
    elif tree_checker.is_same(getattr(bin_tree1, "_BinaryTree__root"),
                              getattr(bin_tree2, "_BinaryTree__root")):
        print("Binary Trees are identical to each other.")
    else:
        print("Binary Trees are not related to each other.")

    # removing a random value from each tree
    if bin_tree1.remove(3):
        print("Removed value 3 from binary tree 1.")
    print("Inorder Traversal:", end=" ")
    bin_tree1.inorder()
    if bin_tree2.remove(8):
        print("\nRemoved value 8 from binary tree 2.")
    print("Inorder Traversal:", end=" ")
    bin_tree2.inorder()

    # comparing bin_tree1 and bin_tree2 again
    if tree_checker.is_mirror(getattr(bin_tree1, "_BinaryTree__root"),
                              getattr(bin_tree2, "_BinaryTree__root")):
        print("\nBinary Trees are mirrors of each other.\n")
    elif tree_checker.is_same(getattr(bin_tree1, "_BinaryTree__root"),
                              getattr(bin_tree2, "_BinaryTree__root")):
        print("\nBinary Trees are identical to each other.\n")
    else:
        print("\nBinary Trees are not related to each other.\n")

    # building bin_tree3
    setattr(bin_tree3, "_BinaryTree__root", node.Node())
    root = getattr(bin_tree3, "_BinaryTree__root")
    setattr(root, "_Node__data", 3)
    setattr(root, "_Node__left_child", node.Node())
    root_left_child = getattr(root, "_Node__left_child")
    setattr(root_left_child, "_Node__data", 8)
    setattr(root, "_Node__right_child", node.Node())
    root_right_child = getattr(root, "_Node__right_child")
    setattr(root_right_child, "_Node__data", 5)
    setattr(root_left_child, "_Node__left_child", node.Node())
    setattr(getattr(root_left_child, "_Node__left_child"), "_Node__data", 9)
    setattr(root_left_child, "_Node__right_child", node.Node())
    setattr(getattr(root_left_child, "_Node__right_child"), "_Node__data", 7)
    setattr(root_right_child, "_Node__left_child", node.Node())
    setattr(getattr(root_right_child, "_Node__left_child"), "_Node__data", 1)
    setattr(root_right_child, "_Node__right_child", node.Node())
    setattr(getattr(root_right_child, "_Node__right_child"), "_Node__data", 6)
    print("\nBinary Tree 3")
    print("Inorder Traversal:  ", end=" ")
    bin_tree3.inorder()
    print("\nPreorder Traversal: ", end=" ")
    bin_tree3.preorder()
    print("\nPostorder Traversal:", end=" ")
    bin_tree3.postorder()
    print('\n')

    # building bin_tree4
    setattr(bin_tree4, "_BinaryTree__root", node.Node())
    root = getattr(bin_tree4, "_BinaryTree__root")
    setattr(root, "_Node__data", 3)
    setattr(root, "_Node__left_child", node.Node())
    root_left_child = getattr(root, "_Node__left_child")
    setattr(root_left_child, "_Node__data", 8)
    setattr(root, "_Node__right_child", node.Node())
    root_right_child = getattr(root, "_Node__right_child")
    setattr(root_right_child, "_Node__data", 5)
    setattr(root_left_child, "_Node__left_child", node.Node())
    setattr(getattr(root_left_child, "_Node__left_child"), "_Node__data", 9)
    setattr(root_left_child, "_Node__right_child", node.Node())
    setattr(getattr(root_left_child, "_Node__right_child"), "_Node__data", 7)
    setattr(root_right_child, "_Node__left_child", node.Node())
    setattr(getattr(root_right_child, "_Node__left_child"), "_Node__data", 1)
    setattr(root_right_child, "_Node__right_child", node.Node())
    setattr(getattr(root_right_child, "_Node__right_child"), "_Node__data", 6)
    print("Binary Tree 4")
    print("Inorder Traversal:  ", end=" ")
    bin_tree4.inorder()
    print("\nPreorder Traversal: ", end=" ")
    bin_tree4.preorder()
    print("\nPostorder Traversal:", end=" ")
    bin_tree4.postorder()
    print('\n')

    # comparing bin_tree3 and bin_tree4
    if tree_checker.is_mirror(getattr(bin_tree3, "_BinaryTree__root"),
                              getattr(bin_tree4, "_BinaryTree__root")):
        print("Binary Trees are mirrors of each other.")
    elif tree_checker.is_same(getattr(bin_tree3, "_BinaryTree__root"),
                              getattr(bin_tree4, "_BinaryTree__root")):
        print("Binary Trees are identical to each other.")
    else:
        print("Binary Trees are not related to each other.")

    # removing a value from each tree
    if bin_tree3.remove(9):
        print("Removed value 9 from binary tree 3.")
    print("Inorder Traversal:", end=" ")
    bin_tree3.inorder()
    if bin_tree4.remove(9):
        print("\nRemoved value 9 from binary tree 4.")
    print("Inorder Traversal:", end=" ")
    bin_tree4.inorder()

    # comparing bin_tree3 and bin_tree4 again
    if tree_checker.is_mirror(getattr(bin_tree3, "_BinaryTree__root"),
                              getattr(bin_tree4, "_BinaryTree__root")):
        print("\nBinary Trees are mirrors of each other.\n")
    elif tree_checker.is_same(getattr(bin_tree3, "_BinaryTree__root"),
                              getattr(bin_tree4, "_BinaryTree__root")):
        print("\nBinary Trees are identical to each other.\n")
    else:
        print("\nBinary Trees are not related to each other.\n")
