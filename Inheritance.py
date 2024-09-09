class Father:
    def __init__(self,eyes,happy):
        self.eyes=eyes
        self.happy=happy

class Son(Father):
    def __init__(self, name, age, eyes, happy):
        self.name = name
        self.age = age
        super().__init__(eyes, happy)

obj = Son("jivin",12,2,True)
print(obj.name)