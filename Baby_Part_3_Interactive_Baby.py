from datetime import date


class Baby:

    def __init__(self, baby_name, birth_date=None, starting_weight=130, starting_height=20):
        
        self.baby_name = baby_name
        self.birth_date = birth_date
        self.starting_weight = starting_weight
        self.starting_height = starting_height
        self.weight = starting_weight      
        self.mood = "content"
        self.eat_count = 0
        self.drink_count = 0
        self.feeding_count = 0           


    def laugh(self):
        self.mood = "happy"
        print(self.baby_name + " is laughing")

    def cry(self):
        self.mood = "sad"
        print(self.baby_name + " is crying")

    def sleep(self):
        self.mood = "content"
        print(self.baby_name + " is sleeping")

    def scream(self):
        self.mood = "mad"
        print(self.baby_name + " is screaming")

    def burp(self):
        self.mood = "happy"
        print(self.baby_name + " burped")

    def poop(self):
        self.weight = self.weight - 5
        self.mood = "uncomfortable"
        print(self.baby_name + " pooped")

    def pee(self):
        self.weight = self.weight - 4
        self.mood = "uncomfortable"
        print(self.baby_name + " peed")


    def eat(self, food="vegetables"):
        self.weight = self.weight + 11
        self.eat_count = self.eat_count + 1
        self.feeding_count = self.feeding_count + 1
        print(self.baby_name + " is eating " + food)

        
        if food == "fruit" or food == "goodies":
            self.laugh()
        elif food == "vegetables":
            self.cry()
        elif food == "cereal":
            self.sleep()
        else:
            self.mood = "content"

        if self.eat_count % 3 == 0:
            self.poop()

        if self.feeding_count % 3 == 0:
            self.burp()

    def drink(self):
        self.mood = "content"
        self.weight = self.weight + 8
        self.drink_count = self.drink_count + 1
        self.feeding_count = self.feeding_count + 1
        print(self.baby_name + " is drinking")

        if self.drink_count % 3 == 0:
            self.pee()

        if self.feeding_count % 3 == 0:
            self.burp()


    def display_status(self):
        OUNCES_PER_POUND = 16
        current_pounds = self.weight / OUNCES_PER_POUND
        print("Here is a summary of your baby's information.")
        print("baby's name: " + self.baby_name)
        print(f"{self.baby_name}'s birth date is: {self.birth_date}")
        print(f"{self.baby_name} ate {self.eat_count} times")
        print(f"{self.baby_name} drank {self.drink_count} times")
        print(f"{self.baby_name} was fed {self.feeding_count} times in total")
        print(f"{self.baby_name}'s weight in ounces is: {self.weight}")
        print(f"{self.baby_name}'s weight in pounds is: {current_pounds}")
        print(f"{self.baby_name}'s height in inches is: {self.starting_height}")
        print(f"{self.baby_name}'s mood is {self.mood}")
        

def ask_int(prompt):
     while True:
        try:
            value = int(input(prompt).strip())
            if value <= 0:
                print("Please enter a number greater than 0.")
                continue
            return value
        except ValueError:
            print("That's not a valid whole number. Please try again.")

def ask_float(prompt):
    while True:
        try:
            value = float(input(prompt).strip())
            if value <= 0:
                print("Please enter a number greater than 0.")
                continue
            return value
        except ValueError:
            print("That's not a valid number. Please try again.")

def ask_date(prompt):
    while True:
        date= (input(prompt).strip())
        if len(date) == 8 and date.isdigit():
            return date
        else:
            ValueError
            print("Please enter exactly 8 numbers, like 08262019.")

print("Hello, and welcome to baby prep!")
print("First, let's gather some information about your baby. Please answer the following questions:")
baby_name = input("What is your baby's name? ")
birth_date = ask_date("What is your baby's birth date (8 numbers, MMDDYYYY)? ")
starting_weight= ask_int("What is your baby's weight in ounces? ")
baby_height = ask_float("What is your baby's height in inches? ")
action= "choose"

while action !="home":
    baby_a= Baby(baby_name=baby_name,birth_date=birth_date,starting_weight=130,starting_height=20) 

    action = input ("What would you like the baby to do? Choose from: eat, drink, sleep, cry, status, or home. ").lower()

    if action == "eat":
       baby_a.eat()

    elif action == "drink":
        baby_a.drink()

    elif action == "sleep":
        baby_a.sleep()

    elif action == "cry":
        baby_a.cry()

    elif action =="status":
         baby_a.display_status()

    elif action == "home":
        break

    else:
        print ("Unknown action, please try again.")
