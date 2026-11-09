from datetime import date


class Baby:

    def __init__(self, baby_name, birth_date=None, starting_weight=130, starting_height=20):
        if birth_date is None:
            birth_date = date.today().isoformat()
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
        print()




print("Test A - Three Eats")
baby_a = Baby("Avery")
baby_a.eat()
baby_a.eat()
baby_a.eat()
baby_a.display_status()


print("Test B - Three Drinks")
baby_b = Baby("Jordan")
baby_b.drink()
baby_b.drink()
baby_b.drink()
baby_b.display_status()


print("Test C - Mixed Feedings")
baby_c = Baby("Riley")
baby_c.eat("fruit")
baby_c.drink()
baby_c.eat("cereal")
baby_c.display_status()

