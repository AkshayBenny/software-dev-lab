class Purchase:
    def __init__(self, customer_id, item_id, amount_paid=float):
        self.customer_id = customer_id
        self.item_id = item_id
        self.amount_paid = float(amount_paid)


class Customer:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.purchases = []

    def add_purchase(self, purchase):
        if purchase.customer_id == self.id:
            self.purchases.append(purchase)

    def get_purchases_table(self):
        table = "item_id\tamount_paid\n"
        for purchase in self.purchases:
            table += f"{purchase.item_id}\t{purchase.amount_paid}\n"
        return table

    def total_amount_paid(self):
        total = sum(purchase.amount_paid for purchase in self.purchases)
        return total


customers = [
    Customer(1, "John", "Doe"),
    Customer(2, "Jane", "Doe"),
]

purchases = [
    Purchase(3, 1, 100),
    Purchase(2, 3, 123),
]

for purchase in purchases:
    for customer in customers:
        if purchase.customer_id == customer.id:
            customer.add_purchase(purchase)
            break

print(customers[0].get_purchases_table())

print(
    f"Total amount paid by {customers[0].first_name}: ${customers[0].total_amount_paid()}")
