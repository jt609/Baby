from datetime import date


class Baby:

    def __init__(self, baby_name, birth_date=None, starting_weight=130, starting_height=20):
        if birth_date is None:
            birth_date = date.today().isoformat()
        self.baby_name = baby_name
        self.birth_date = birth_date
        self.starting_weight = starting_weight
        self.starting_height = starting_height
        self.mood = "content"
        self.eat_count = 0
        self.drink_count = 0

    def cry(self):
        self.mood = "sad"
        print (self.baby_name + " is crying")

    def sleep(self):
        self.mood ="content"
        print (self.baby_name + " is sleeping")

    def laugh(self):
        self.mood ="happy"
        print (self.baby_name + " is laughing")

    def display_status(self):
        OUNCES_PER_POUND = 16
        current_pounds = self.starting_weight / OUNCES_PER_POUND
        print("Here is a summary of your baby's information.")
        print("baby's name: " + self.baby_name)
        print(f"{self.baby_name}'s birth date is: {self.birth_date}")
        print(f"{self.baby_name} ate {self.eat_count} times")
        print(f"{self.baby_name} drank {self.drink_count} times")
        print(f"{self.baby_name}'s weight in pounds is: {current_pounds}")
        print(f"{self.baby_name}'s height in inches is: {self.starting_height} ")
        print(f"{self.baby_name}'s mood is {self.mood}")


baby1 = Baby("Avery")
baby2 = Baby("Jordan", starting_weight=140)

baby1.display_status()
baby2.display_status()



