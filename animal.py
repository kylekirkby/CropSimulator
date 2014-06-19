class Animal:

    """ This is the super class for animals """

    def __init__(self, growth_rate, light_need, water_need, food_need):

        #attributes

        self._weight = 1
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._food_need = food_need
        self._water_need = water_need
        self._status = "Newly Born"
        self._type = "Generic"

    def needs(self):
        return {'light need':self._light_need,'water need':self._water_need}

    
    def report(self):
        #returns a dict containing type,status, growth and days growing
        return {'type':self._type,'status':self._status,'growth':self._growth,'days growing':self._days_growing}
    
    def _update_status(self):
        if self._growth > 15:
            self._status = "Old"
        elif self._growth > 10:
            self._status = "Mature"
        elif self._growth > 5:
            self._status = "Young"
        elif self._growth > 0:
            self._status = "Baby"
        elif self._growth == 0:
            self._status = "Newly Born"


    def grow(self,light,water, food):

        
        if light >= self._light_need and water >= self._water_need and food >= self._food_need:
            self._growth += self._growth_rate

        #inc days growing
        self._days_growing += 1
        
        self._update_status()

def auto_grow(crop, days):
    #grow the crop over a number of days

    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        crop.grow(light,water)

def manual_grow(animal):
   valid = False
   while not valid:
      try:
         light = int(input("Please enter a light value (1-10): "))
         if 1 <= light <= 10:
            valid = True
         else:
            print("Value entered not valid - please enter a light value between 1 and 10")
      except ValueError:
         print("Value entered not valid - please enter a light value between 1 and 10")
   valid = False
   while not valid:
      try:
         water = int(input("Please enter a water value (1-10): "))
         if 1 <= light <= 10:
            valid = True
         else:
            print("Value entered not valid - please enter a water value between 1 and 10")
      except ValueError:
         print("Value entered not valid - please enter a water value between 1 and 10")
         
   valid = False
   while not valid:
      try:
         water = int(input("Please enter a food value (1-10): "))
         if 1 <= light <= 10:
            valid = True
         else:
            print("Value entered not valid - please enter a food value between 1 and 10")
      except ValueError:
         print("Value entered not valid - please enter a food value between 1 and 10")

   animal.grow(light, water, food)
         
#tests the functionality of the class manually



def display_menu():
   print("1. Grow manually over 1 day")
   print("2. Grow automatically over 30 days")
   print("3. Report Status")
   print("0. Exit Program")
   print()
   print("Please select an option from the above menu")

def get_menu_choice():
   option_valid = False
   while not option_valid:
      try:
         choice = int(input("Option Selected: "))
         if 0 <= choice <= 4:
            option_valid = True
         else:
            print("Please enter a valid option")
      except ValueError:
         print("Please enter a valid option")
   return choice

def manage_crop(animal):
   
   print("This is the animal management program")
   print()
   noexit = True
   while noexit:
      display_menu()
      option = get_menu_choice()
      print()
      if option == 1:
         manual_grow(animal)
         print()
      elif option == 2:
         auto_grow(animal, 30)
         print()
      elif option == 3:
         print(animal.report())
         print()
      elif option == 0:
         noexit = False
         print()
   print("Thank you for using the animal management program!")

   
def main():
   
   
    #instantiate class

   new_animal = Animal(1,4,3,4)

   manage_animal(new_animal)

    

if __name__ == "__main__":

    main()
