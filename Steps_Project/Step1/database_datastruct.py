
class AVLTree():
    def __init__(self):
        self.node = None
        self.height = -1
        self.balance = 0

    def insert(self, player):
        if self.node == None:
            self.node = player
            self.node.right = AVLTree()
            self.node.left = AVLTree()
        elif player.score > self.node.score:
            self.node.right.insert(player)
        else:
            self.node.left.insert(player)
        self.rebalance()

    def delete(self, player):
        if self.node != None:
            if self.node.name == player.name:
                # If we find the key in the leaf node, we erase the player. 
                if not self.node.left.node and not self.node.right.node:
                    self.node = None
                # Node has only one subtree (right), replacing the root
                elif not self.node.left.node:                
                    self.node = self.node.right.node
                # Node has only one subtree (left), replacing the root
                elif not self.node.right.node:
                    self.node = self.node.left.node
                else:
                    # Find  successor as smallest node in right subtree or
                    # predecessor as largest node in left subtree
                    successor = self.node.right.node  
                    while successor and successor.left.node:
                        successor = successor.left.node

                    if successor:
                        self.node = successor
                        # Delete successor from the replaced node right subree
                        self.node.right.delete(successor)

            elif player.score <= self.node.score:
                self.node.left.delete(player)

            elif player.score > self.node.score:
                self.node.right.delete(player)

            # Rebalancing the tree after deleting the players so that we have a balanced tree. 
            self.rebalance()

    def rebalance(self):
        """
        Rebalance tree
        After inserting or deleting a node, we have to check if the node is balanced and 
        update it so that we respect the AVL Tree's conditions. 
        """
        # Check if we need to rebalance the tree
        self.update_heights(recursive=False)
        self.update_balances(False)

        # For each node checked, 
        #   if the balance factor remains −1, 0, or +1 then no rotations are necessary.
        while self.balance < -1 or self.balance > 1: 
            # Left subtree is larger than right subtree
            if self.balance > 1:

                # Left Right Caseif self.node.left.balance < 0:self.node.left.rotate_left()
                self.update_heights()
                self.update_balances()

                self.rotate_right()
                self.update_heights()
                self.update_balances()
            
            # Right subtree is larger than left subtree
            if self.balance < -1:
                
                # Right Left Case
                if self.node.right.balance > 0:
                    self.node.right.rotate_right() # we're in case III
                    self.update_heights()
                    self.update_balances()

                # Right Right Case
                self.rotate_left()
                self.update_heights()
                self.update_balances()

    def update_heights(self, recursive=True):
        """
        Update tree height
        Tree height is max height of either left or right subtrees +1 for root of the tree
        """
        if self.node: 
            if recursive: 
                if self.node.left: 
                    self.node.left.update_heights()
                if self.node.right:
                    self.node.right.update_heights()
            
            self.height = 1 + max(self.node.left.height, self.node.right.height)
        else: 
            self.height = -1

    def update_balances(self, recursive=True):
        """
        Calculate tree balance factor
        The balance factor is calculated as follows: 
        balance = height(left subtree) - height(right subtree). 
        """
        if self.node:
            if recursive:
                if self.node.left:
                    self.node.left.update_balances()
                if self.node.right:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def rotate_right(self):
        """
        Right rotation
        set self as the right subtree of left subree
        """
        new_root = self.node.left.node
        new_left_sub = new_root.right.node
        old_root = self.node

        self.node = new_root
        old_root.left.node = new_left_sub
        new_root.right.node = old_root

    def rotate_left(self):
        """
        Left rotation
        set self as the left subtree of right subree
        """
        new_root = self.node.right.node
        new_left_sub = new_root.left.node
        old_root = self.node

        self.node = new_root
        old_root.right.node = new_left_sub
        new_root.left.node = old_root
    
    def inorder_traverse(self):
        """
        Inorder traversal of the tree to return a list of each
        Player() object contained in the AVL tree
        """
        result = []

        if not self.node:
            return result

        result.extend(self.node.left.inorder_traverse())
        result.append(self.node)
        result.extend(self.node.right.inorder_traverse())

        return result

    def get_min(self):
        # return the objet from Player() with the minimum score
        current = self.node
        while current.left.node is not None:
            current = current.left.node
        return current
