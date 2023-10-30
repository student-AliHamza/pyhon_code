class Cash_and_carry:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        self.products.append({
            'name': name,
            'price': price,
            'quantity': quantity
        })

    def display_details(self):
        print("Product Details:")
        for product in self.products:
            print(f"Name: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}")

    



# Example usage
cash_and_carry = Cash_and_carry()

while True:
    product_name = input("Enter the name of the product: ")
    price = int(input("Enter the price of the product: "))
    quantity = int(input("Enter the quantity of the product: "))
    operation = input("Press 'y' to see details, 'n' to continue: ")

    cash_and_carry.add_product(product_name, price, quantity)

    if operation.lower() == 'y':
        cash_and_carry.display_details()
        break  # Exit the loop after displaying details
    elif operation.lower() == 'n':
        continue
