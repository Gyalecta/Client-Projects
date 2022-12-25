class MindMap:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def remove_node(self, node):
        self.nodes.remove(node)

    def find_node(self, text):
        for node in self.nodes:
            if node.text == text:
                return node
        return None
