from node import Node

class BinarySearchTree:

    """
    initializer: initializes the attribute root
    """
    def __init__(self):
        self.__root = None

    """
    preorder(): traverses in the order root, left, right
    creates a stack and pushes root onto it
    loops until stack is empty:
        pops from the stack and prints its data
        pushes right child, then left child onto the stack
        so that left child is popped and printed first
    """
    def preorder(self):
        if self.__root is None:
            return
        stack = []
        stack.append(self.__root)
        while stack:
            temp = stack.pop()
            print(getattr(temp, "_Node__data"), end=" ")
            if getattr(temp, "_Node__right_child") is not None:
                stack.append(getattr(temp, "_Node__right_child"))
            if getattr(temp, "_Node__left_child") is not None:
                stack.append(getattr(temp, "_Node__left_child"))

    """
    inorder(): traverses in the order left, root, right
    creates a stack
    loops until temp is None and the stack is empty:
        pushes temp onto the stack
        traverses left by setting temp to temp's left child
        once traversed left, pops temp from stack and prints it
        sets temp to temp's right child
    """
    def inorder(self):
        if self.__root is None:
            return
        temp = self.__root
        stack = []
        while True:
            if temp is not None:
                stack.append(temp)
                temp = getattr(temp, "_Node__left_child")
            elif stack:
                temp = stack.pop()
                print(getattr(temp, "_Node__data"), end=" ")
                temp = getattr(temp, "_Node__right_child")
            else:
                break

    """
    postorder(): traverses in the order left, right, root
    creates 2 stacks
    pushes root onto stack1
    loops until stack1 is empty:
        pops temp from stack1
        pushes temp onto stack2
        pushes temp's left child then temp's right child onto stack1
        so that when they are pushed and popped from stack2, 
        they are printed in the correct order
    """
    def postorder(self):
        if self.__root is None:
            return
        stack1 = []
        stack2 = []
        stack1.append(self.__root)
        while stack1:
            temp = stack1.pop()
            stack2.append(temp)
            if getattr(temp, "_Node__left_child"):
                stack1.append(getattr(temp, "_Node__left_child"))
            if getattr(temp, "_Node__right_child"):
                stack1.append(getattr(temp, "_Node__right_child"))
        while stack2:
            node = stack2.pop()
            print(getattr(node, "_Node__data"), end=" ")

    """
    insert(): inserts the nodes in the correct order based on their values
    if root is none, makes temp a node and sets temp's data to data
    otherwise, loops until temp is None:
        sets parent of temp to temp, so when temp reaches the end of the tree,
        parent is referencing where to insert the new node
        if data < temp's data, then traverses left
        if data > temp's data, then traverses right
    if data is less than parent's data:
        sets parent's left child to be a node and sets it's data to data
    if data is greater than parent's data:
        sets parent's right child to be a node and sets it's data to data
    """
    def insert(self, data):
        if self.__root is None:
            temp = Node()
            setattr(temp, "_Node__data", data)
            return temp
        temp = self.__root
        parent = None
        while temp is not None:
            parent = temp
            if data < getattr(temp, "_Node__data"):
                temp = getattr(temp, "_Node__left_child")
            else:
                temp = getattr(temp, "_Node__right_child")
        if data < getattr(parent, "_Node__data"):
            setattr(parent, "_Node__left_child", Node())
            setattr(getattr(parent, "_Node__left_child"), "_Node__data", data)
        else:
            setattr(parent, "_Node__right_child", Node())
            setattr(getattr(parent, "_Node__right_child"), "_Node__data", data)
        return self.__root

    """
    remove(): removes a given node from the tree
    calls the search() method to check if the given node is in the tree
    if given node to be removed has 0 or 1 child:
        if left child exists, sets new_temp to be the right child
        if left child doesn't exist, sets new_temp to be the left child
        the new_temp node will replace the node to be removed
    if given node to be removed has 2 children:
        find inorder successor of temp by finding the minimum value in the 
        subtree with temp's right child. 
        the inorder successor will replace the node to be removed
        if succ isn't the root, set parent's left child to succ's right child
        if succ is the root, set temp's right child to succ's right child
        then set temp's data to succ's data
        
    """
    def remove(self, data):
        temp, parent = self.search(data)
        if temp == -1:
            print("\nTried to remove the value", data)
            print("but value not found in binary search tree.")
            return False
        if getattr(temp, "_Node__left_child") is None or \
                getattr(temp, "_Node__right_child") is None:
            if getattr(temp, "_Node__left_child") is None:
                new_temp = getattr(temp, "_Node__right_child")
            else:
                new_temp = getattr(temp, "_Node__left_child")
            if parent is None:
                return True
            if temp == getattr(parent, "_Node__left_child"):
                setattr(parent, "_Node__left_child", new_temp)
            else:
                setattr(parent, "_Node__right_child", new_temp)
        else:
            succ = getattr(temp, "_Node__right_child")
            succ, p_succ = self.get_min(succ)
            if p_succ is not None:
                setattr(p_succ, "_Node__left_child",
                        getattr(succ, "_Node__right_child"))
            else:
                setattr(temp, "_Node__right_child",
                        getattr(succ, "_Node__right_child"))
            setattr(temp, "_Node__data", getattr(succ, "_Node__data"))
        return True
    """
    search(): traverses through the tree, searching for given data
    loops until temp reaches the end of the tree or temp = data
        if data is greater than temp's data, then traverse right
        if data is less than temp's data, then traverse left
    returns either the temp node and the parent of temp node
    or -1 values to show that the data was not found
    """
    def search(self, data):
        temp = self.__root
        parent = None
        while temp is not None and getattr(temp, "_Node__data") != data:
            parent = temp
            if data > getattr(temp, "_Node__data"):
                temp = getattr(temp, "_Node__right_child")
            elif data < getattr(temp, "_Node__data"):
                temp = getattr(temp, "_Node__left_child")
        if temp is None:
            return -1, -1
        elif getattr(temp, "_Node__data") == data:
            return temp, parent

    """
    get_min(): finds the maximum value in the tree
    traverses right until temp reaches the rightmost leaf node
    returns the temp node, which has the maximum value, and it's parent
    """
    def get_max(self, root):
        if root is None:
            return
        temp = root
        parent = None
        while temp is not None and \
                getattr(temp, "_Node__right_child") is not None:
            parent = temp
            temp = getattr(temp, "_Node__right_child")
        return temp, parent
    """
    get_min(): finds the minimum value in the tree
    traverses left until temp reaches the leftmost leaf node
    returns the temp node, which has the minimum value, and it's parent
    """
    def get_min(self, root):
        if root is None:
            return
        temp = root
        parent = None
        while temp is not None and \
                getattr(temp, "_Node__left_child") is not None:
            parent = temp
            temp = getattr(temp, "_Node__left_child")
        return temp, parent
