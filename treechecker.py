class TreeChecker:

    """
    is_mirror(): checks if 2 trees are mirrors of each other
    creates a stack
    loops until roots are None and stack is empty:
        while root1 and root2 are not None:
            compares root1 and root2's data
            pushes roots onto stack
            root1 in tree 1 traverses left and root2 in tree 2 traverses right
        once at least one of the trees has been traversed, compares again
        if stack is not empty:
            pops roots from stack and loops again traversing trees in the
            opposite direction this time
    """
    def is_mirror(self, root1, root2):
        stack = []
        while True:
            while root1 and root2:
                if getattr(root1, "_Node__data") != \
                        getattr(root2, "_Node__data"):
                    return False
                stack.append(root2)
                stack.append(root1)
                root1 = getattr(root1, "_Node__left_child")
                root2 = getattr(root2, "_Node__right_child")
            if root1 is None and root2 is not None:
                return False
            if root1 is not None and root2 is None:
                return False
            if stack:
                root1 = stack.pop()
                root2 = stack.pop()
                root1 = getattr(root1, "_Node__right_child")
                root2 = getattr(root2, "_Node__left_child")
            else:
                break
        return True

    """
    is_same(): checks if 2 trees are identical to each other
    compares roots
    creates a stack and pushes roots onto it
    loops until stack is empty:
        pops temps from both trees from stack and compares their data
        if they are equal, pushes temps left children, 
        then right children onto stack and loops again
    """
    def is_same(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        elif root1 is None:
            return False
        elif root2 is None:
            return False
        stack = []
        stack.append(root1)
        stack.append(root2)
        while stack:
            temp2 = stack.pop()
            temp1 = stack.pop()
            if getattr(temp1, "_Node__data") != getattr(temp2, "_Node__data"):
                return False
            if getattr(temp1, "_Node__left_child") and \
                    getattr(temp2, "_Node__left_child"):
                stack.append(getattr(temp1, "_Node__left_child"))
                stack.append(getattr(temp2, "_Node__left_child"))
            elif getattr(temp1, "_Node__left_child") or \
                    getattr(temp2, "_Node__left_child"):
                return False
            if getattr(temp1, "_Node__right_child") and \
                    getattr(temp2, "_Node__right_child"):
                stack.append(getattr(temp1, "_Node__right_child"))
                stack.append(getattr(temp2, "_Node__right_child"))
            elif getattr(temp1, "_Node__right_child") or \
                    getattr(temp2, "_Node__right_child"):
                return False
        return True
