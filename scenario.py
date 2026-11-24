class Vehicle:
    def __init__(self, number, brand, price):
        self.number = number
        self.brand = brand
        self.price = price

    def display(self):
        print("Vehicle Number:", self.number)
        print("Brand:", self.brand)
        print("Price:", self.price)

        if self.price >= 1000000:
            print("Category: Luxury")
        else:
            print("Category: Economy")


class Showroom:
    def __init__(self):
        self.v1 = None
        self.v2 = None

    def add_vehicles(self):
        print("Enter First Vehicle Details")
        n = input("Vehicle Number: ")
        b = input("Brand: ")
        p = int(input("Price: "))
        self.v1 = Vehicle(n, b, p)

        print("Enter Second Vehicle Details")
        n = input("Vehicle Number: ")
        b = input("Brand: ")
        p = int(input("Price: "))
        self.v2 = Vehicle(n, b, p)

    def display_vehicles(self):
        print("\nVehicle Details:")
        self.v1.display()
        self.v2.display()


s = Showroom()
s.add_vehicles()
s.display_vehicles()
