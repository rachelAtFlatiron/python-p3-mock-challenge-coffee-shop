from statistics import mean 

class Coffee:
    def __init__(self, name):
        self.name = name

    @property 
    #get
    def name(self):
        #'_' indicates it is a private variable
        return self._name
    #set
    @name.setter #don't forget setter decorator
    def name(self, name):
        if(not hasattr(self, 'name') and isinstance(name, str) and len(name) > 2):
            self._name = name 
        else: 
            raise Exception
    
        
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        # return list(set([order.customer for order in self.orders()]))
        # Order.all -> match coffee
        return list(set([order.customer for order in Order.all if order.coffee == self]))
    
    def num_orders(self):
        #return len([order for order in Order.all if order.coffee == self])
        return len(self.orders())
    
    def average_price(self):
        #make use of self.orders
        listOfOrders = self.orders()
        return (sum([curOrder.price for curOrder in listOfOrders]))/len(listOfOrders)
        # return sum([order.price for order in self.orders()]) / self.num_orders()
        #return mean([order.price for order in self.orders()])

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
        #constraints 
        if(isinstance(name, str) and 1 <= len(name) <= 15):
            self._name = name 
        else:
            raise Exception

    @classmethod 
    def most_aficionado(cls, coffee):
        greatest_customer = None 
        greatest_sum = 0

        #look through all customers  
        for customer in Customer.all:
            #look through all the orders 
            sum = 0
            for order in Order.all:
                #find the orders where order.customer == current customer and order.coffee == coffee (passed in as an arg)
                if(order.customer == customer and order.coffee == coffee):
                    #increment sum + order.price 
                    sum += order.price
            #compare current sum to greatest_sum 
            if(greatest_sum < sum):
                #update greatest customer and greatest_sum 
                greatest_sum = sum 
                greatest_customer = customer 
        return greatest_customer

        # #getting all the coffee orders
        # coffee_orders = [order for order in Order.all if order.coffee == coffee]
        # coffee_dict = {}
        # #iterating over all order's of current coffee
        # #iterating over all the Orders
        # #and matching them up based on customer
        # for coffee_order in coffee_orders:
        #     #iterating over Order.all and summing the orders.price where the current order's customer matches the current coffee order
        #     coffee_dict[coffee_order.customer] = sum([orders.price for orders in Order.all if orders.customer == coffee_order.customer and orders.coffee == coffee])
        # return max(coffee_dict, key=lambda x: coffee_dict[x])



    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        #return list(set([order.coffee for order in self.orders()]))
        return list({order.coffee for order in self.orders()})
    
    def create_order(self, coffee, price):
        new_order = Order(self, coffee, price)
        return new_order
    
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
        if(not hasattr(self, "price") and isinstance(price, float) and 1.0 < price < 10.0):
            self._price = price 
        else: 
            raise Exception

    def __repr__(self):
        return f'<Order belongs to {self.customer.name} of {self.coffee.name}>'