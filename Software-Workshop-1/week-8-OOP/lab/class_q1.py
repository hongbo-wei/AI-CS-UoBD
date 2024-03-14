class Airplane:
    def __init__(self, fuel, seatingCapacity, company, engineType) -> None:
        self.fuel = fuel
        self.seatingCampacity = seatingCapacity
        self.company = company
        self.engineType = engineType

    def boarding(self, number):
        if number < 0:
            print("Invalid input")
        else:
            if number > self.seatingCampacity:
                print("Overloaded")
            else:
                print("Not overloaded")

    def fueling(self, amount):
        self.fuel += amount
        print(f"After adding fuel, the airplane has {self.fuel}.")

emirates = Airplane(2000, 200, "Emirates", "Ramjet and Scramjet Engines")
print(f"{emirates.company} airplane can load {emirates.seatingCampacity} people, \
the engine type is {emirates.engineType}, its fuel capacity is {emirates.fuel}.")
emirates.boarding(199)
emirates.fueling(500)

flyDubai = Airplane(1000, 100, "Fly Dubai", "Turbofan Engines")
print(f"{flyDubai.company} airplane can load {flyDubai.seatingCampacity} people, \
the engine type is {flyDubai.engineType}, its fuel capacity is {flyDubai.fuel}.")
flyDubai.boarding(150)
flyDubai.fueling(200)