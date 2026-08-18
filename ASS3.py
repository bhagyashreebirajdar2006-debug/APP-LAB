class PaymentStrategy:
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")


class DebitCardPayment(PaymentStrategy):
    def pay(self, amount):
        print("Paid", amount, "using Debit Card")


class UpiPayment(PaymentStrategy):
    def pay(self, amount):
        print("Paid", amount, "using UPI")


class CashPayment(PaymentStrategy):
    def pay(self, amount):
        print("Paid", amount, "using Cash")


class PaymentProcessor:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        if self.strategy is None:
            print("No payment method selected")
        else:
            self.strategy.pay(amount)


processor = PaymentProcessor()

print("Payment Methods")
print("1. Credit Card")
print("2. Debit Card")
print("3. UPI")
print("4. Cash")

choice = int(input("Enter your choice: "))
amount = float(input("Enter amount: "))

if choice == 1:
    processor.set_strategy(CreditCardPayment())
elif choice == 2:
    processor.set_strategy(DebitCardPayment())
elif choice == 3:
    processor.set_strategy(UpiPayment())
elif choice == 4:
    processor.set_strategy(CashPayment())
else:
    print("Invalid choice")

processor.process_payment(amount)
