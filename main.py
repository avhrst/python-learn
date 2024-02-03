class Car:
    def __init__(self, brand, model,year, color):
        self.brand = brand
        self.model = model
        self.__year = year
        self.color = color
        
        
    @property
    def year(self):
        return self.__year
 
    @year.setter
    def year(self, year):
        if year < 1900:
            print("Year is not valid")
        else:
            self.__year = year    
        
    def start(self):   
        print("Car started")
        
    def stop(self):    
        print("Car stopped")         

class ElectricCar(Car):
    def __init__(self, brand, model,year, color, battery):
        super().__init__(brand, model,year, color)
        self.battery = battery
        
    def start(self):
        print("Electric car started")
        
    def stop(self):
        print("Electric car stopped") 
 


# Testing 
car1 = Car("Toyota", "Corolla", 2015, "Black")
print(car1.year)
car1.year = 2020
print(car1.year)
car1.year = 1800
print(car1.year)

car2 = ElectricCar("Tesla", "Model S", 2019, "Red", 100)
print(car2.year)
car2.year = 2020
print(car2.year)
car2.year = 1800

car2.start()
car2.stop()


