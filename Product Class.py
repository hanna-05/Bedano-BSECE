class Inventory:
    def __init__(self, product_id, name, product_description, price, quantity):
        self.product_id = product_id
        self.name = name
        self.product_description = product_description
        self.price = price
        self.quantity = quantity

products = []

def add_product():
    product_id = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    product_description = input("Enter Product Description: ")
    price = float(input("Enter the Product Price: "))
    quantity = int(input("Enter Product Quantity: "))
    products.append(Inventory(product_id, name, product_description, price, quantity))
    print("Product added successfully!\n")

def update_stock():
    product_id = input("Enter Product ID to update: ")
    product = next((prd for prd in products if prd.product_id == product_id), None)
    
    if product:
        print(f"Updating quantity for {product.name} ({product.product_id})")
        product.quantity = int(input("Enter new Product Quantity: "))
        print("Product Quantity updated successfully!\n")
    else:
        print("Product not found!\n")

def display_all():
    if not products:
        print("No Products in inventory.")
        return
    for prd in products:
        print(f'Product Name: {prd.name}, Product ID: {prd.product_id}, Product Description: {prd.product_description}, Price: {prd.price}, Quantity: {prd.quantity}')
    print()

def calculate_inventory():
    total_inventory = 0
    for prd in products:
        total_value = prd.price * prd.quantity
        total_inventory += total_value
    print(f'Total Value of Inventory: {total_inventory:.2f}\n')

def main():
    while True:
        print("Inventory Management System")
        print("1. Add Product")
        print("2. Update Stocks")
        print("3. Display All Products")
        print("4. Calculate Inventory Value")
        print("5. Exit the Program")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_product()
        elif choice == "2":
            update_stock()
        elif choice == "3":
            display_all()
        elif choice == "4":
            calculate_inventory()
        elif choice == "5":
            print("Exiting Program! Thank you!")
            break
        else:
            print("Invalid Choice. Please Try Again!\n")

if __name__ == "__main__":
    main()
