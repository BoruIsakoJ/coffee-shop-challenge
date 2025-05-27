class Coffee:
    def __init__(self, name):
        if type(name)== str and len(name)>=3:
            self._name = name    
        else:
            raise ValueError("Coffee name must be a string and should be at least 3 characters")
        self._orders =[]
    @property
    def name(self):
        return self._name
    

    def orders(self):
        return self._orders
    
    def customers(self):
        return list(set(order.customer for order in self._orders))

    def num_orders(self):
        return len(self._orders)
    
    def average_price(self):
        if not self._orders:
            return 0
        return sum(order.price for order in self._orders) / len(self._orders)

# coffee1 = Coffee("Arabica")
# print(coffee1.name)
# coffee1.name = "Robusta" rauses this error "AttributeError: can't set attribute" when uncommented