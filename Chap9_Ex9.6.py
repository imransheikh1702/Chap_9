class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.res_name = restaurant_name
        self.cus_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        a = self.res_name.title() + " serves " + self.cus_type + "."
        print("\n" + a)

    def open_restaurant(self):
        a = self.res_name.title() + " is open. Welcome!"
        print("\n" + a)

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type= 'Ice Cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
    
    def display_flavors(self):
        print("\nFollowing flavors are available today: \n")
        for flavor in self.flavors:
            print(" * " + flavor.title())
            
scoop = IceCreamStand('The Scoop')
scoop.flavors = ['chocolate', 'strawberry', 'vanilla']

scoop.describe_restaurant()
scoop.open_restaurant()
scoop.display_flavors()

