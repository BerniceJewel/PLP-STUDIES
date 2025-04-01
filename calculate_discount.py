def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Parameters:
    price (float): The original price
    discount_percent (float): The discount percentage
    
    Returns:
    float: The final price after discount (if applicable)
    """
    if discount_percent >= 20:
        # Apply the discount if it's 20% or higher
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        # Return original price if discount is less than 20%
        return price

# Get user input
original_price = float(input("Enter the original price: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount_percentage)
# Display the result 
print(f"The final price after applying the discount is: {final_price:.2f}")
# Example usage
# original_price = 100.00
# discount_percentage = 20.0
# final_price = calculate_discount(original_price, discount_percentage)