#Program for E-Commerce platform
def add_product(product_name, price, quantity):
    # Create a dictionary object for the product with the given parameters
    product = {
        "product_name": product_name,
        "price": price,
        "quantity": quantity
    }
    return product

def update_price(product, new_price):
    # Update the price of the product in the dictionary
    product["price"] = new_price
    return product

def update_quantity(product, quantity_change):
    # Update the quantity of the product in the dictionary
    product["quantity"] += quantity_change
    return product

# Test the functions
product1 = add_product("Laptop", 999.99, 10)
print("Initial Product 1:", product1)

product1 = update_price(product1, 899.99)
print("Updated Price Product 1:", product1)

product1 = update_quantity(product1, -2)
print("Updated Quantity Product 1:", product1)
