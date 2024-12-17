# Dependency
class Payment:
    def __init__(self, amount):
        self.amount = amount

    def process_payment(self):
        print(f"Processing payment of ${self.amount}.")

class Order:
    def __init__(self, order_id, amount):
        self.order_id = order_id
        self.amount = amount

    def place_order(self):
        print(f"Placing order #{self.order_id}.")
        payment = Payment(self.amount)  # Dependency
        payment.process_payment()

# Dependency
order = Order(101, 250.50)
order.place_order()