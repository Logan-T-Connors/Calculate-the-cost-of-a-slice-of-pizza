# Constants
CHEESE_SLICE_COST = 3.50
PEPPERONI_SLICE_COST = 4.50
HST_RATE = 0.13
SHOP_RENT_COST = 1.00
MATERIALS_COST = 0.50

# Function to calculate total cost
def calculate_total_cost(pizza_type, num_slices):
		if pizza_type.lower() == "cheese": 
				slice_cost = CHEESE_SLICE_COST
		elif pizza_type.lower() == "pepperoni":
				slice_cost = PEPPERONI_SLICE_COST
		else:
				print("Invalid pizza type. Please choose Cheese or Pepperoni.")
				return

		# Calculate total cost
		total_cost = (slice_cost + MATERIALS_COST + SHOP_RENT_COST) * num_slices

		# Add HST
		total_cost_with_hst = total_cost * (1 + HST_RATE)

		# Print the result
		print(f"The total cost for {num_slices} {pizza_type} slices is: ${total_cost_with_hst:.2f}")

# Input from user
pizza_type_input = input("Enter the pizza type (Cheese or Pepperoni): ")
num_slices_input = input("Enter the number of slices: ")

# Convert num_slices_input to integer, handle invalid input
try:
		num_slices = int(num_slices_input)
except ValueError:
		print("Invalid input for the number of slices. Please enter a valid number.")
		num_slices = 0

# Calculate and display the total cost
calculate_total_cost(pizza_type_input, num_slices)
