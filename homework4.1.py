class Product:
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = float(price)
        self.quantity = int(quantity)

    def change_price(self, new_price):
        self.price = float(new_price)

    def change_quantity(self, new_quantity):
        self.quantity = int(new_quantity)

    def __str__(self):
        return f"{self.name} | {self.category} | Price: {self.price} | Quantity: {self.quantity}"


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def __str__(self):
        return f"{self.name} | {self.email} | Orders: {len(self.orders)}"


class Order:
    def __init__(self):
        self.products = []
        self.total_price = 0

    def add_product(self, product):
        if product.quantity > 0:
            self.products.append(product)
            product.quantity -= 1
            self.calculate_total()
        else:
            print(f"{product.name} is out of stock")

    def calculate_total(self):
        total = 0

        for product in self.products:
            total += product.price

        self.total_price = total
        return self.total_price

    def __str__(self):
        product_names = []

        for product in self.products:
            product_names.append(product.name)

        return f"Products: {product_names} | Total: {self.total_price}"


def load_products_from_file(filename):
    products = []
    with open (filename, "r") as file:
        for line in file:
            name, category, price, quantity = line.strip().split(",")
            product = Product(name, category, float(price), int(quantity))
            products.append(product)
    return products
        


def load_customers_from_file(filename):
    customers = []

    with open (filename, "r") as file:
        for line in file:
            name, email = line.strip().split(",")

            customer = Customer(name, email)
            customers.append(customer)

    return customers


products = load_products_from_file("products.txt")
customers = load_customers_from_file("customers.txt")


print("Products in shop:")
for product in products:
    print(product)


print("\nCustomers:")
for customer in customers:
    print(customer)


order1 = Order()

order1.add_product(products[0])
order1.add_product(products[1])

customers[0].add_order(order1)


print("\nOrder information:")
print(order1)

print("\nCustomer after order:")
print(customers[0])

print("\nProducts after order:")
for product in products:
    print(product)
