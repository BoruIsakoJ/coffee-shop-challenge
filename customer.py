# from order import Order  was bringing this error "(most likely due to a circular import)"
class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if type(name)==str and 1<=len(name)<=15:
            self._name = name
            
        else:
            raise ValueError("Customer name must be a string and should be between 1-15 characters")

    @property
    def orders(self):
        return self._orders
    
    def coffees(self):
        return list(set(order.coffee for order in self._orders))
  
    def create_order(self, coffee, price):
        from order import Order
        return Order(customer=self, coffee=coffee,price=price)
   
    @classmethod
    def most_aficionado(cls, coffee):
        if not coffee._orders:
            return None
        spending = {}
        for order in coffee._orders:
            customer = order.customer
            spending[customer] = spending.get(customer, 0) + order.price
        return max(spending, key=spending.get)
   
 
# customer1 = Customer("Boru")
# print(customer1.name)
