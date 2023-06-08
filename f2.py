from f1 import *
class ShoppingCart:
    def __init__(self):
        self.items = []
        
    def add_item(self,product,price,quantity):
        item=CartItem(product,price,quantity)
        self.items.append(item)
    
    def remove_item(self,product):
        for item in self.items:
            if item.product == product:
                self.items.remove(item)
                print("--------Item removed successfully---------")
    
    def update_item_quantity(self,product):
        for item in self.items:
            if item.product == product:
                item.quantity = 2
    
    def view_cart(self):
        if len(self.items)==0:
            print("Cart is empty")
        else:
            for item in self.items:
                print("Product:",item.product,"Price:",item.price,"Quantity:",item.quantity)
    
    def total_cost(self):
        total=0
        for item in self.items:
            total+=item.price*item.quantity
        print("Total Cost is :",total)
        
    def reset_cart(self):
        if len(self.items)==0:
            print("Cart is empty")
        else:
            p=self.items
            p.clear()
            print("-------Remove all items from cart successfully-------")
            print("Shopping Cart",self.items)

    def empty_cart(self):
        if len(self.items)==0:
            print("-------Cart is empty-------")
        else:
            print("------Cart is not empty-----")