print("---Welcome to Checkout Machine---")
base_price = float(input("Enter price: "))
tax_rate = float(input("Enter tax rate: "))
item_count = int(input("Enter the item count: "))

subtotal = base_price * item_count
total_price = subtotal + (subtotal * (tax_rate/100))

is_expensive = total_price >= 500.0
print(total_price)
print(is_expensive)
print(type(is_expensive))