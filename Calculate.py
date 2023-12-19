#Variables
Diameter = int(input("Enter the diameter of the Pizza: "))
pizza_type_input = input("Enter the pizza type (Cheese or Pepperoni): ")

# Constants
CHEESE_SLICE_COST = 0.50
PEPPERONI_SLICE_COST = 1.50
HST_RATE = 0.13
SHOP_RENT_COST = 1.00
MATERIALS_COST = 0.50

def calculate_total_cost(pizza_type, diameter):
		if pizza_type.lower() == "cheese": 
				slice_cost = CHEESE_SLICE_COST
		elif pizza_type.lower() == "pepperoni":
				slice_cost = PEPPERONI_SLICE_COST
		else:
				print("Invalid pizza type. Please choose Cheese or Pepperoni.")
				return

		# Calculate total cost
		total_cost = (slice_cost + MATERIALS_COST + SHOP_RENT_COST) * diameter

		# Add HST
		total_cost_with_hst = total_cost * (1 + HST_RATE)

		# Print the result
		print(f"The total cost for {diameter} Inch {pizza_type} slice is: ${total_cost_with_hst:.2f}")

# Calculate and display the total cost
calculate_total_cost(pizza_type_input, Diameter)
