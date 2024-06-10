class Coffee:
    def __init__(self, name):
        #make sure to use the property setter, not self._name
        self.name = name
        
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list(set([order.customer for order in self.orders()]))
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        #all the prices
        # sum = 0
        # for order in self.orders():
        #     sum += order.price
        total = sum([order.price for order in self.orders()])
         #divide by number of orders
        return total/self.num_orders()

    @property 
    def name(self):
        return self._name 
    
    @name.setter 
    def name(self, new_name):
        #check if _name has already been created
        if(hasattr(self, 'name')):
            return 'no'
        else:
            #create it
            self._name = new_name

    def __repr__(self):
        return f'<Coffee name={self.name} />'

class Customer:
    def __init__(self, name):
        self.name = name
    
    @classmethod
    def sum_coffee_orders(cls, coffee, customer):
        #filter through orders for matching coffee/customer pairs
        coffee_orders = [order for order in Order.all if order.coffee == coffee and order.customer == customer]
        #sum above prices
        return sum([order.price for order in coffee_orders])

    @classmethod 
    def most_aficionado(cls, coffee):
        # all customer orders
        # filter for matching coffee orders
        coffee_orders = [order for order in Order.all if order.coffee == coffee]
        if(len(coffee_orders) == 0):
            return None
        # sum orders per customer
        # cf: current coffee order that max is iterating over
        return(max(coffee_orders, key=lambda cf: Customer.sum_coffee_orders
        (coffee, cf.customer))).customer
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        #order contains information regarding coffee 
        return list(set([order.coffee for order in self.orders()]))
    
    def create_order(self, coffee, price):
        new_order = Order(self, coffee, price)
        return new_order

    @property 
    def name(self):
        return self._name 
    
    @name.setter 
    def name(self, new_name):
        if(isinstance(new_name, str) and 1 <= len(new_name) <= 15):
            self._name = new_name 
        else:
            print('no')

    def __repr__(self):
        return f'<Customer name={self.name} />'
    
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property 
    def price(self):
        return self._price 
    
    @price.setter 
    def price(self, new_price):
        if(not hasattr(self, 'price') and isinstance(new_price, float) and 1.0 <= new_price <= 10.0):
            self._price = new_price 
        else:
            print('no')

    def __repr__(self):
        return f'<Order customer={self.customer} coffe={self.coffee} price={self.price} />'