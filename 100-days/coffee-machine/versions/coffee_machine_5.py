'''Coffee Machine Project'''
import json
import os

class Coffee:
    def __init__(self, name, water, milk, beans):
        self.name = name
        self.water = water #ml
        self.milk = milk #ml
        self.beans = beans #grams

class CoffeeMachine:
    def __init__(self, water, milk, beans):
        self.water = water
        self.milk = milk
        self.beans = beans

        self.menu = {}

        self.uses_since_descale = 0
        self.warning_limit = 10
        self.lock_limit = 15
        self.islocked = False

        self.max_water = 1500 #ml
        self.max_milk = 800 #ml
        self.max_beans = 500 #grams

    def add_drink(self,coffee):
        self.menu[coffee.name.lower()] = coffee

    def load_state(self):
        if not os.path.exists(self.state_file):
            return  # first run, nothing to load

        with open(self.state_file, "r") as f:
            data = json.load(f)

        self.water = data.get("water", self.water)
        self.milk = data.get("milk", self.milk)
        self.beans = data.get("beans", self.beans)
        self.uses_since_descale = data.get("uses_since_descale", 0)
        self.islocked = data.get("islocked", False)
        self.coffee_counts = data.get("coffee_counts", {})

    def save_state(self):
        data = {
            "water": self.water,
            "milk": self.milk,
            "beans": self.beans,
            "uses_since_descale": self.uses_since_descale,
            "islocked": self.islocked,
            "coffee_counts": self.coffee_counts
        }

        with open(self.state_file, "w") as f:
            json.dump(data, f, indent=4)


    def show_menu(self):
        print("\nAvailable drinks")
        for drink_name, coffee in self.menu.items():
            print("-", drink_name.title())
            if (self.water < coffee.water):
                print(f"Not available. Minimum of {coffee.water - self.water}ml more water required.")
            if (self.beans < coffee.beans):
                print(f"Not available. Minimum of {coffee.beans - self.beans}g more beans required.")
            if (self.milk < coffee.milk):
                print(f"Not available. Minimum of {coffee.milk - self.milk}ml more milk required.")

    def status(self):
        print("\nMachine Status")
        print(f"Water: {self.water}/{self.max_water} ml")
        print(f"Milk: {self.milk}/{self.max_milk} ml")
        print(f"Beans: {self.beans}/{self.max_beans} g")
        print(f"Uses since last descale: {self.uses_since_descale}")

        if self.islocked:
            print("Machine locked. Descaling required.")
        elif self.uses_since_descale >= self.warning_limit:
            print("Descale Warning.)")

    def can_make(self,coffee):
        if self.water < coffee.water:
            return f"A minimum of {self.water - coffee.water}ml of water has to be added. Add {self.max_water - self.water} to restore full capacity."
        if self.beans < coffee.beans:
            return f"A minimum of {self.beans - coffee.beans}g of beans has to be added. Add {self.max_beans - self.beans} to restore to full capacity."
        if self.milk < coffee.milk:
            return f"A minimum of {self.milk - coffee.milk}ml of milk has to be added. Add {self.max_milk - self.milk} to restore to full capacity."
    def check_descaling(self):
        if self.uses_since_descale >= self.lock_limit:
            self.islocked = True
            print("Machine locked. Descaling required.")
        elif self.uses_since_descale >= self.warning_limit:
            print("Warning. Descaling required.")

        #make coffee
    def make_coffee(self,coffee_name):
        if self.islocked:
            print("Cannot make coffee. Descaling required.")
            return
        coffee_name = coffee_name.lower()

        if coffee_name not in self.menu:
            print("Drink unavailable")
            return
        coffee = self.menu[coffee_name]
        issues = self.can_make(coffee)

        if issues:
            print("\nCannot make coffee.")
            print(issues)
            return
        
        self.water -= coffee.water
        self.milk -= coffee.milk
        self.beans -= coffee.beans
        self.uses_since_descale += 1
        self.coffee_counts[coffee_name] = self.coffee_counts.get(coffee_name, 0) + 1

        print(f"Your {coffee_name} is ready!")
        self.check_descaling() #shows warning if descaling required

        self.save_state()

    def refill_status(self):
        print(f'''
        Recommended refill amounts:
        Water: {self.max_water - self.water} ml
        Milk:  {self.max_milk - self.milk} ml
        Beans: {self.max_beans - self.beans} g
        ''')


    def refill(self, water=0, milk=0, beans=0): #default value 0 if no input
        
              
              
              
        if self.water + water > self.max_water:
            print("Water exceeds tank limit.")
        else:
            self.water += water
            print(f"Refill successful! Status of water tank is {self.water}ml.")
        if self.milk + milk > self.max_milk:
            print("Milk exceeds tank limit.")
        else:
            self.milk += milk
            print(f"Refill successful! Status of milk tank is {self.milk}ml.")
        if self.beans + beans > self.max_beans:
            print("Beans exceed hopper limit.")
        else:
            self.beans += beans
            print(f"Refill successful! Status of hopper is {self.beans}g.")

        self.save_state()

    def descale(self):
        self.uses_since_descale = 0
        self.islocked = False
        print("Machine descaled successfully!")
        self.save_state()
    def show_stats(self):
        print("\nCoffee usage stats:")
        if not self.coffee_counts:
            print("No coffee made yet.")
            return

        for coffee, count in self.coffee_counts.items():
            print(f"- {coffee.title()}: {count}")


#Setup

machine = CoffeeMachine(water=500,milk=300,beans=200)
machine.load_state()

machine.add_drink(Coffee("Espresso", 30, 0, 8))
machine.add_drink(Coffee("Latte", 200, 150, 12))
machine.add_drink(Coffee("Flat White", 150, 100, 12))
machine.add_drink(Coffee("Cappuccino", 200, 100, 12))
machine.add_drink(Coffee("Macchiato", 50, 20, 8))
machine.add_drink(Coffee("Milk", 0, 200, 0))

while True:
    
    print("\n1. Show menu.")
    print("2. Make coffee")
    print("3. Refill machine")
    print("4. Show status")
    print("5. Descale machine")
    print("6. Show Stats")
    print("7. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        machine.show_menu()
    elif choice == '2':
        drink = input("Enter drink name: ")
        machine.make_coffee(drink)

    elif choice == '3':
        machine.refill_status()
        w = int(input("Add water (ml):  "))
        m = int(input("Add milk (ml):  "))
       #y                                          #iykyk
        b = int(input("Add coffee beans"))
        machine.refill(water=w,milk=m,beans=b)

    elif choice == '4':
        machine.status()

    elif choice == '5':
        machine.descale()

    elif choice == '6':
        machine.show_stats()

    elif choice == '7':
        print("Machine turned off.")
        break
    else:
        print("Invalid choice.")










