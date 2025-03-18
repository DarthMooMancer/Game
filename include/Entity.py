class Entity:
    def __init__(self):
        pass
        # Test using git from neovim

class EntityManager(Entity):
    def __init__(self, window):
        super().__init__()
        self.groups = []
        self.window = window

    def addGroup(self, name):
        self.groups.append(name)

    def removeGroup(self, name):
        self.groups.remove(name)

    def addToGroup(self, nameOfObject, nameOfGroup):
        for i in self.groups:
            if i == nameOfGroup:
                nameOfGroup.add(nameOfObject)

    def update(self):
        for i in self.groups:
            i.draw(self.window)
            i.update()
