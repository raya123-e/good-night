
#Parent class/Superclass
class animal:
    def speak(self):
        print('Animal is speaking')


    #Child class/Sub /derived class
class dog(animal):
    def bark(self):
        print('Dog id barking')


class cat(dog):
    def meow(self):
        print('Car is meowing')



a = animal()
d = dog()
c= cat()
