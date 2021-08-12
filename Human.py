class Human:
    """Can start with an input of (name, age, children, parents) """
    name = ''
    age = 0
    children = []
    parents = []

    def __init__(self, input_name=name, input_age=age, input_children=children, input_parents=parents):
        """created parent child connections if not already established"""
        if len(input_children) > 0:
            for child in input_children:
                if self not in child.parents:
                    child.add_parent(self)
        if len(input_parents) > 0:
            for parent in input_parents:
                if (self not in parent.children):
                    parent.has_child(self)

        self.name = input_name
        self.age = input_age
        self.children = input_children
        self.parents = input_parents

    def has_birthday(self):
        self.age += 1
        print(f'Happy Birthday{self.name}! You are {self.age} years old!')

    def has_child(self, child):
        if self.age < 18:
            print(f'Sorry, {self.name} is too young to have kids')
        else:
            self.children.append(child)
            child.add_parent(self)

    def add_parent(self, parent):
        self.parents.append(parent)

    def get_age(self):
        print(f'{self.name} is {self.age} years old')

    def get_parents(self):
        pass
        # print(f'{self.name}parents are {self.parents[0].name}')


bob = Human('Bob', 1)
sally = Human('Sally', 22, [bob])
bob.has_birthday()
bob.get_age()
sally.get_age()
sally.has_birthday()
bob.get_parents()

print(sally.children[0].name)
print(bob.parents[0].name)
