class Node:
    def __init__(self, text, x=0, y=0):
        self.text = text
        self.x = x
        self.y = y
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def edit(self, new_text):
        self.text = new_text
