# arraylist.py

class ArrayList:
    def __init__(self):
        self.data = []

    def add(self, value):
        self.data.append(value)

    def get(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of range")
        return self.data[index]

    def size(self):
        return len(self.data)
