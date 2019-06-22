from abc import ABC,abstractmethod

class animal(ABC):
    @abstractmethod
    def move(self):
        pass

class human(animal):
    def move(self):
        print('I can walk')

class snake(animal):
    def move(self):
        print('I can crawal')

obj1=human();
obj2=snake();
obj3=animal();


obj1.move();
obj2.move();
