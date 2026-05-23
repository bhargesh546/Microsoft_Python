
def main():
	
    full_price = price_input("Enter price: ")
	
    # Call function for members
    member_price = calc_sale_price(full_price, True)
    print("Member price:",member_price)

    # Call function for non-members
    non_member_price = calc_sale_price(full_price, False)
    print("Non-member price:",non_member_price)
	
def price_input(prompt):
	while True:
		try:
			price = float(input(prompt))
			
			# Check if the price is positive (logical validation)
			if price < 0:
				print("Price cannot be negative.")
				continue
			return price
		except ValueError:
			print("Invalid Input Enter only numbers: ")

def calc_sale_price(amount: float, member: bool) -> float:
	if member:
		# Members receive a 15% discount (0.15)
		amount = amount - (amount * 0.15)
	else:
		# Non-members get a 5% discount (0.05)
		amount = amount - (amount * 0.05)

	# Round amount to two decimal places
	# Save back in the amount variable
	amount = round(amount, 2)

	# Return amount to the main program
	return amount

# Example price (already provided)
# full_price = 150.50

if __name__ == "__main__":
	main()