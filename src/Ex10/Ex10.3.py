class Smith:
    surname = "Smith"
    profession = "smith"

    def __init__(self, name, profession=None):
        self.name = name
        if profession is not None:
            self.profession = profession

#name is always an instance attribute which is set in the constructor, and each class instance can have a different name value
#surname is always a class attribute, and cannot be overridden in the constructor – every instance will have a surname value of Smith
#profession is a class attribute, but it can optionally be overridden by an instance attribute in the constructor. Each instance will have a profession value of smith unless the optional surname parameter is passed into the constructor with a different value.