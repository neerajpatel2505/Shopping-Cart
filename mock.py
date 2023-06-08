from f2 import *

cart=ShoppingCart()
# Adding an item to the shopping cart
cart.add_item("Laptop",50000,1)
cart.add_item("Cable",500,10)
cart.add_item("Cell",50,15)

# Viewing/listing the content of the shopping cart
cart.view_cart()

# Updating the desired quantity of an item from the shopping cart
cart.update_item_quantity("Laptop")

# Viewing/listing the content of the shopping cart
cart.view_cart()

# Removing an item from the shopping cart
cart.remove_item("Laptop")
cart.view_cart()
#Checking if the shopping cart is empty
cart.empty_cart()

# Calculating the total cost of the shopping cart
cart.total_cost()

# Emptying/Resetting the shopping cart,
cart.reset_cart()

#Checking if the shopping cart is empty
cart.empty_cart()
            