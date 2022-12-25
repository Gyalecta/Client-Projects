import tkinter as tk

from mind_map.node import Node
from mind_map.mind_map import MindMap

class App:
    def __init__(self):
        # Create the main window
        self.root = tk.Tk()
        self.root.title('Mind Map Maker')

        # Create a canvas for displaying the mind map
        self.canvas = tk.Canvas(self.root, width=600, height=400)
        self.canvas.pack()

        # Create a mind map object
        self.mind_map = MindMap()

        # Create a button for adding new nodes
        self.add_node_button = tk.Button(self.root, text='Add Node', command=self.add_node)
        self.add_node_button.pack()

    def add_node(self):
        # Create a new node
        node = Node('New Node')

        # Add the node to the mind map
        self.mind_map.add_node(node)

        # Redraw the mind map on the canvas
        self.draw_mind_map()

    def draw_mind_map(self):
        # Clear the canvas
        self.canvas.delete('all')

        # Iterate over the nodes in the mind map
        for node in self.mind_map.nodes:
            # Calculate the x and y coordinates for the node
            x = node.x * 100 + 50
            y = node.y * 100 + 50

            # Draw the node on the canvas
            self.canvas.create_oval(x-50, y-50, x+50, y+50, fill='white')
            self.canvas.create_text(x, y, text=node.text)

            # Iterate over the child nodes of the current node
            for child in node.children:
                # Calculate the x and y coordinates for the child node
                child_x = child.x * 100 + 50
                child_y = child.y * 100 + 50

                # Draw a line connecting the current node to the child node
                self.canvas.create_line(x, y, child_x, child_y)

    def run(self):
        # Start the event loop
        self.root.mainloop()

def edit_node(self):
    # Get the text of the selected node
    node_text = self.selected_node.text

    # Create a dialog box for entering the new node text
    text_entry = tk.Entry(self.root)
    text_entry.insert(0, node_text)
    text_entry.pack()

    # Create a button for submitting the new node text
    submit_button = tk.Button(self.root, text='Submit', command=lambda: self.submit_edit(text_entry, submit_button))
    submit_button.pack()


def submit_edit(self, text_entry, submit_button):
    # Get the new node text from the text entry widget
    new_text = text_entry.get()

    # Update the text of the selected node
    self.selected_node.edit(new_text)

    # Redraw the mind map on the canvas
    self.draw_mind_map()

    # Destroy the text entry and submit button widgets
    text_entry.destroy()
    submit_button.destroy()



if __name__ == '__main__':
    # Create an instance of the App class and start the application
    app = App()
    app.run()
