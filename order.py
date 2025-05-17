from customer import Customer
from coffee import Coffee

class Order:
    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise Exception("Customer must be an instance of Customer")
        if not isinstance(coffee, Coffee):
            raise Exception("Coffee must be an instance of Coffee")
        if not type(price)== float or not (1.0 <= price <= 10.0):
            raise Exception("Price must be a float between 1.0 and 10.0")        
        
        self._customer = customer
        self._coffee = coffee
        self._price = price
        customer._orders.append(self)
        coffee._orders.append(self)
        
    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price
    
    
customer1 = Customer("Boru")
coffee1 = Coffee("Arabica")
order1 = customer1.create_order(coffee1, 3.5)

customer2 = Customer("Isako")
order2 = customer2.create_order(coffee1, 9.5)

print("Customer Name:",customer1.name)  
print("Coffee Name:",coffee1.name)  
print("Coffee Price:",order1.price)  
print("Customer Orders:",customer1.orders())  
print("No. of orders:",coffee1.num_orders())  
print("Average price",coffee1.average_price())  
print("Customers:",coffee1.customers())   