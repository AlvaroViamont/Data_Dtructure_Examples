class Node:
    def __init__(self, valor=0, father=None, left=None, right=None) -> None:
        self.father = father
        self.left = left
        self.right = right
        
        self.valor = valor



class BinaryTree:
    def __init__(self, node:Node) -> None:
        self.root = node
    
    def add_node(self, node:Node):
        if node.valor < self.root.valor:
            if not self.root.left:
                self.root.left = node
                node.father = self.root
            else:
                self._add_recursive_node(node, self.root.left)
        else:
            if not self.root.right:
                self.root.right = node
                node.father = self.root
            else:
                self._add_recursive_node(node, self.root.right)

    def _add_recursive_node(self, node:Node, father:Node):
        if node.valor < father.valor:
            if not father.left:
                father.left = node
                node.father = father
            else:
                self._add_recursive_node(node, father.left)
        else:
            if not father.right:
                father.right = node
                node.father = father
            else:
                self._add_recursive_node(node, father.right)
    
    def search_element(self, element):
        if self.root.valor == element:
            return True, self.root
        else:
            if self.root.left:
                result, element = self._search_recursive_element(element, self.root.left)
                if result:
                    return result, element
            if self.root.right:
                result, element = self._search_recursive_element(element, self.root.right)
                if result:
                    return result, element
            return False, None
    
    def _search_recursive_element(self, element, father:Node):
        if father.valor == element:
            return True, father
        else:
            if father.left:
                result, element = self._search_recursive_element(element, father.left)
                if result:
                    return True, father
            if father.right:
                result, element = self._search_recursive_element(element, father.right)
                if result:
                    return True, father
            return False, None