# nie ma klasy BST, ale napiszę jej szklielet dla lepszje przejrzystości

class BinarySearchTree:
    class BST_node:
        def __init__(self, dat = None, l = None, r = None):
            self.data = dat
            self.left = l
            self.right = r


    def __init__(self):
        self.root = self.BST_node
        self.elements_cnt = 0


    def bst_max(self, top):
        if self.elements_cnt == 0:
            raise ValueError
        else:
            temp = self.root
            while temp.right != None:
                temp = temp.right

            return temp
            
    def bst_min(self, top):
        if self.elements_cnt == 0:
            raise ValueError
        else:
            temp = self.root
            while temp.left != None:
                temp = temp.left

            return temp