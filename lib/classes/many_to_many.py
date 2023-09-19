class Coffee:
    def __init__(self, name):
        self.name = name
        
    @property 
    def name(self):
        return self._name 

    @name.setter 
    def name(self, name):
        if not hasattr(self, "name") and isinstance(name, str) and len(name) >= 3:
            self._name = name 
        else:
            raise Exception

    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list(set([order.customer for order in Order.all if order.coffee == self]))

    def num_orders(self):
        return len([order for order in Order.all if order.coffee == self])
    
    def average_price(self):
        sum = 0 
        for i in self.orders():
            sum += i.price 
        return sum/(len(self.orders()))

class Customer:
    all = []

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)
    
    @property
    def name(self):
        return self._name
    @name.setter 
    def name(self, name):
        if(isinstance(name, str) and 1 <= len(name) <= 15):
            self._name = name 
        else:
            raise Exception
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return list(set([order.coffee for order in self.orders()]))
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    
    @classmethod
    def most_aficionado(self, coffee):
        #for each customer
        most_customer = None
        most_price = 0
        for customer in Customer.all:
            #get all the orders with matching customer, and matching coffee 
            customer_orders = [order for order in customer.orders() if order.coffee == coffee]
            #sum the price
            price = 0
            for order in customer_orders:
                price += order.price
            if price > most_price:
                most_price = price 
                most_customer = customer 
        return most_customer 
    
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
    def price(self, price):
        if not hasattr(self, "price") and 1.0 <= price <= 10.0:
            self._price = price
        else: 
            raise Exception