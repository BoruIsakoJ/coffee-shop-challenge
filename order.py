from customer import Customer
from coffee import Coffee

class Order:
    def __init__(self, customer, coffee, price):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise ValueError("Customer must be an instance of Customer")
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise ValueError("Coffee must be an instance of Coffee")
        if isinstance(price, (float, int)) and (1.0 <= price <= 10.0):
            self._price = float(price)
        else:
            raise ValueError("Price must be a float between 1.0 and 10.0")        
        
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
    

if __name__ == "__main__":
    try:
        customer1 = Customer("Boru")
        coffee1 = Coffee("Capuccino")
        order1 = customer1.create_order(coffee1, 3.5)
        

        customer2 = Customer("Isako")
        order2 = customer2.create_order(coffee1, 2.5)
        order3 = customer2.create_order(coffee1, 8.5)

        print("Customer Name:", customer2.name)
        print("Coffee Name:", coffee1.name)
        print("Coffee Price:", order2.price)
        print("Customer Orders:", customer2.orders)
        print("No. of orders:", coffee1.num_orders())
        print("Average price", coffee1.average_price())
        print("Customers:", coffee1.customers())
        print("Top Customer for this coffee:", Customer.most_aficionado(coffee1).name)
    except ValueError as e:
        print("Error during object creation:", e)
    except AttributeError as e:
        print("Attribute error:", e)