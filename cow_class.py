from animal import *

class Cow(Animal):

    """ This is a cow """

    def __init__(self, name):
        #default values for  cow to be instantiated = growth_Rate = 1;
        #light_need = 5; water_need = 6; food_need = 3;
        
        super().__init__(1,5,6,3,name = "Jim")

        self._type = "Cow"


        
    def grow(self, food, water):

        if water >= self._water_need and food >= self._food_need:

            if self._status == "Newly Born":

                self._growth += self._growth_rate * 2
                
            elif self._status == "Baby":
                
                self._growth += self._growth_rate * 1.5

            elif self._status == "Young":

                self._growth += self._growth_rate * 1.25
                

            else:

                self._growth += self._growth_rate

        #increment days growing

        self._days_growing += 1

        #update status

        self._update_status()
        
