def calculate_discount(price, discount_percent):
    # Check if the discount is 30% or higher
   
    if discount_percent == 30:
     discounted_money = price * (discount_percent / 100)
     new_price = price - discounted_money
     return new_price
    else:
        return price

# Prompt the user for input
price = float(input("Please enter the item price price of the item: "))
discount_percent = float(input("Please enter your 30 percent discount: "))

# Calculate and print the final price
new_price = calculate_discount(price, discount_percent)

print(f"The final price after applying the discount is: R{new_price:.2f}")