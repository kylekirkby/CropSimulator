from animal import *

class Sheep(Animal):

    """ This is a sheep """

    def __init__(self):
        #default values for  sheep to be instantiated = growth_Rate = 1;
        #light_need = 4; water_need = 5; food_need = 4;
        
        super().__init__(1,4,5,4)

        self._type = "Sheep"


        
    def grow(self, light, water, food):

        if light >= self._light_need and water >= self._water_need and food >= self._food_need:

            if self._status == "Newly Born":

                self._growth += self._growth_rate * 1.75

                self._weight += self._growth_rate * 10.75
                
            elif self._status == "Baby":
                
                self._growth += self._growth_rate * 1.5

                self._weight += self._growth_rate * 10.5

            elif self._status == "Young":

                self._growth += self._growth_rate * 1.25

                self._weight += self._growth_rate * 10.25
                

            else:

                self._growth += self._growth_rate

                self._weight += self._growth_rate

        #increment days growing

        self._days_growing += 1

        #increment size

        #update status

        self._update_status()
        
