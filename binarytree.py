class BinaryTree:
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
    remove(): removes a given node from the tree
    checks if there is only 1 node in the tree and if it is equal to data
    otherwise, creates a queue and enqueues root
    loops until queue is empty:
        dequeues temp from queue
        if temp's data is equal to data, sets data's node to be temp
        otherwise, enqueues temp's left child then right child
        eventually temp will equal the deepest, rightmost node
    after the loop, if data was found in the tree:
        repeats a similar loop, but searches for temp and deletes it
    the data of the node to be removed is replaced with the deepest node's data
    """
    def remove(self, data):
        if self.__root is None:
            return
        if getattr(self.__root, "_Node__left_child") is None and \
           getattr(self.__root, "_Node__right_child") is None:
            if getattr(self.__root, "_Node__data") == data:
                self.__root = None
                return True
            else:
                print("\nTried to remove the value", data)
                print("but value not found in binary tree.")
                return False
        data_node = None
        temp = None
        queue = []
        queue.append(self.__root)
        while queue:
            temp = queue.pop(0)
            if getattr(temp, "_Node__data") == data:
                data_node = temp
            if getattr(temp, "_Node__left_child"):
                queue.append(getattr(temp, "_Node__left_child"))
            if getattr(temp, "_Node__right_child"):
                queue.append(getattr(temp, "_Node__right_child"))
        if data_node:
            deep_val = getattr(temp, "_Node__data")
            deepest = temp
            queue = []
            queue.append(self.__root)
            while queue:
                temp = queue.pop(0)
                if temp is deepest:
                    temp = None
                if getattr(temp, "_Node__right_child"):
                    if getattr(temp, "_Node__right_child") == deepest:
                        setattr(temp, "_Node__right_child", None)
                    else:
                        queue.append(getattr(temp, "_Node__right_child"))
                if getattr(temp, "_Node__left_child"):
                    if getattr(temp, "_Node__left_child") == deepest:
                        setattr(temp, "_Node__left_child", None)
                    else:
                        queue.append(getattr(temp, "_Node__left_child"))
            setattr(data_node, "_Node__data", deep_val)
        else:
            print("\nTried to remove value", data)
            print("but value was not found in binary tree.")
            return False
        return True
