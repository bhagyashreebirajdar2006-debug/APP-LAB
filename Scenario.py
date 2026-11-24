
import csv
import re

class Bank:
    def __init__(self, filename):
        self.filename = filename

    def display(self):
        with open(self.filename, 'r') as f:
            data = csv.DictReader(f)

            for row in data:
                print(row)

    def search(self):
        acc = input("Enter Account Number: ")

        pattern = r'^[0-9]{9,18}$'

        if not re.match(pattern, acc):
            print("Invalid Account Number")
            return

        with open(self.filename, 'r') as f:
            data = csv.DictReader(f)

            for row in data:
                if row['AccountNumber'] == acc:
                    print("Customer Found:")
                    print(row)
                    return

            print("Customer Not Found")


filename = "customers.csv"

b = Bank(filename)

print("1. Display All Customers")
print("2. Search Customer")

ch = int(input("Enter your choice: "))

if ch == 1:
    b.display()
elif ch == 2:
    b.search()
else:
    print("Invalid Choice")
