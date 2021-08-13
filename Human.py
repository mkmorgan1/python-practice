class Human():
    """Can start with an input of (name, age, children, parents) """
    name = ''
    age = 0

    def link_parents(self, parent):
        parent.children.append(self)

    def link_children(self, child):
        child.parents.append(self)

    def __init__(self, input_name=name, input_age=age, ):
        self.children = []
        self.parents = []
        self.name = input_name
        self.age = input_age

    def has_birthday(self):
        self.age += 1
        print(f'Happy Birthday {self.name}! You are {self.age} years old!')

    def add_child(self, child):
        self.children.append(child)
        self.link_children(child)

    def add_parent(self, parent):
        self.parents.append(parent)
        self.link_parents(parent)

    def get_age(self):
        print(f'{self.name} is {self.age} years old')

    def get_parents(self):
        if len(self.parents) > 0:
            names = ''
            for parent in self.parents:
                if names == '':
                    names = parent.name
                else:
                    names += f' & {parent.name}'
            print(f'{self.name}\'s parent(s): {names}.')
        else:
            print(f'{self.name} does not have any parents listed.')

    def get_children(self):
        if len(self.children) > 0:
            names = ''
            for child in self.children:
                if names == '':
                    names = child.name
                else:
                    names += f' & {child.name}'
            print(f'{self.name}\'s children: {names}.')
        else:
            print(f'{self.name} does not have any children listed.')


bob = Human('Bob', 1)
sally = Human('Sally', 22)
sally.add_child(bob)
bob.has_birthday()
sally.has_birthday()
bob.get_parents()
sally.get_parents()
bob.get_children()
sally.get_children()
