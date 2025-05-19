## ☕ Coffee Ordering System

A simple Python project that models the relationships between **Customers**, **Coffees**, and **Orders** using OOP principles like encapsulation, associations, and data validation.

---

### 📁 Project Structure

```
coffee-ordering-system/
├── coffee.py     # Defines the Coffee class
├── customer.py   # Defines the Customer class
├── order.py      # Defines the Order class and runs test code
└── README.md     # Project documentation
```

---

### 🧠 Classes Overview

#### `Customer`

- **Attributes**
  - `name`: string (min 3 characters)
- **Methods**
  - `orders()`: returns all Order instances for the customer
  - `coffees()`: returns a unique list of Coffee instances the customer has ordered
  - `create_order(coffee, price)`: creates and stores a new Order

#### `Coffee`

- **Attributes**
  - `name`: string (min 3 characters)
- **Methods**
  - `orders()`: returns all Order instances for this coffee
  - `customers()`: returns a unique list of customers who’ve ordered this coffee
  - `num_orders()`: returns the number of orders placed for this coffee
  - `average_price()`: returns the average price of all orders (0 if none)

#### `Order`

- **Attributes**
  - `customer`: must be an instance of `Customer`
  - `coffee`: must be an instance of `Coffee`
  - `price`: float (between 1.0 and 10.0)
- **Properties**
  - Read-only access to `customer`, `coffee`, and `price`

---

### 🚀 How to Run

Make sure all `.py` files are in the same folder. Then run:

```bash
python order.py
```

This will execute a test script demonstrating the relationships and functionality.

---

