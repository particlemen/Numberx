
class Numberx:
    def __init__(self,value):
        self.value = value
    def plus(self, n):
        self.value = self.value + n
    def minus(self,n):
        self.value = self.value - n
    def times(self,n):
        self.value = self.value * n
    def divide(self,n):
        self.value = self.value / n
    def mod(self,n):
        self.value = self.value%n
    def value(self):
        return self.value
    
