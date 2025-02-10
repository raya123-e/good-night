class car:
    def __init__(self,color,yom):
        self.color = color
        self.yom = yom


    def drive (self):
          print("You drive",self.color,"car")

car1 = car("Black",2009)
print(car1.color)


car2 = car("Blue",2010)