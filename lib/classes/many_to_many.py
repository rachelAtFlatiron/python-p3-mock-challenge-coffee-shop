import ipdb 
class Coffee:
    def __init__(self, name):
        self.name = name
        
    def orders(self):
        coffee_orders = [] #array with relevant orders
        for order in Order.all:
            if(order.coffee == self):
                coffee_orders.append(order)
        return coffee_orders
    
    def customers(self):
        #the element that we want in the array - customer
        #for loop  - orders 
        #if statement - no
        return list(set([order.customer for order in self.orders()]))
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        #sum of all prices of orders (self.orders())
        #number of orders (self.num_orders())

        # total = 0
        # for order in self.orders():
        #     total += order.price 
        # return total/self.num_orders()

        total = sum([order.price for order in self.orders()]) 
        return total/self.num_orders()

    @property 
    def name(self):
        return self._name 
    @name.getter 
    def name(self):
        return self._name 
    @name.setter 
    def name(self, val):
        if not hasattr(self, 'name') and isinstance(val, str) and len(val) >= 3:
            self._name = val 

    def __repr__(self):
        return f'<Coffee name={self.name} />'
    
class Customer:
    all = []

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)
        
    def orders(self):
        #order
        #Order.all
        #if order.customer == self
        return [order for order in Order.all if order.customer == self]
    
    #get all customer's coffees
    def coffees(self):
        customer_coffees = [] 
        for order in self.orders():
            customer_coffees.append(order.coffee)
        return list(set(customer_coffees))

    
    def create_order(self, coffee, price):
        new_order = Order(price=price, customer=self, coffee=coffee)
        return new_order
    
    @classmethod 
    def most_aficionado(self, coffee):
        #need all customers : Customer.all 
        #all orders for the coffee
        coffee_orders = coffee.orders()
        most_total = -1
        most_customer = None 
        for customer in Customer.all:
            #sum price for all orders in coffee_orders where order.customer == customer 
            current_total = sum([order.price for order in coffee_orders if order.customer == customer])
            if current_total > most_total:
                most_total = current_total 
                most_customer = customer 
        return most_customer

    
    
    def __repr__(self):
        return f'<Customer name={self.name} />'
    

    @property 
    def name(self):
        return self._name 
    @name.getter
    def name(self):
        return self._name 
    @name.setter 
    def name(self, val):
        if isinstance(val, str) and 1 <= len(val) <= 15:
            self._name = val
        else:
            raise Exception

class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)
    
    def __repr__(self):
        return f'<Order customer={self.customer.name} coffee={self.coffee.name} price={self.price} />'
    
    @property 
    def price(self):
        return self._price 
    @price.getter 
    def price(self):
        return self._price 
    @price.setter 
    def price(self, val):
        if isinstance(val, float) and 1.0 <= val <= 10.0 and not hasattr(self, 'price'):
            self._price = val

latte = Coffee('latte')
mocha = Coffee('mocha')
brew = Coffee('brew')

anne = Customer('anne')
george = Customer('george')
lana = Customer('lana')
cristine = Customer('cristine')

order_1 = Order(coffee=latte, customer=anne, price=3.0)
order_2 = Order(coffee=mocha, customer=cristine, price=5.0)
order_3 = Order(coffee=brew, customer=anne, price=1.0)
order_4 = Order(coffee=latte, customer=george, price=7.5)

coffee = Coffee("Vanilla Latte")
coffee_2 = Coffee("Flat White")
customer = Customer("Steve")
Order(customer, coffee, 2.0)
Order(customer, coffee, 2.0)
Order(customer, coffee_2, 5.0)

# ipdb.set_trace()