class Coffee:
    def __init__(self, name):
        self.name = name
        
    def orders(self):
        #look through all the orders
        #find the matching ones
        return [ order for order in Order.all if order.coffee == self ]
    
    def customers(self):
        #look through all matching orders
        #extract the customer
        return list(set([order.customer for order in self.orders()]))
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        if(self.num_orders() == 0):
            return 0
        # total_price = 0 
        #look at each order
        # for order in self.orders():
        #     #sum the price
        #     total_price += order.price 
        # #divide by number of orders to get average 
        # return(total_price/self.num_orders())

        price_list = [order.price for order in self.orders()]
        return sum(price_list)/self.num_orders()

    @property 
    def name(self):
        return self._name 
    @name.setter 
    def name(self, new_name):
        if(hasattr(self, 'name')):
            print("coffee already has a name")
        else:
            self._name = new_name 

    def __repr__(self):
        return f'<Coffee name={self.name} />'

class Customer:
    all = []
    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    def orders(self):
        #look through all orders
        #find ones where order.customer == self 
        return [order for order in Order.all if order.customer == self ]
    
    def coffees(self):
        return list(set([order.coffee for order in self.orders()]))
    
    def create_order(self, coffee, price):
        return Order(coffee=coffee, price=price, customer=self)

    @classmethod 
    def most_aficionado(cls, coffee):
        #return customer that has spent most money on coffee
        ret_customer = None #customer object to return 
        ret_customer_total = 0 #total price for coffees for current customer
        #look through each customer
        for customer in cls.all:
            cur_total = 0
            #find total money spent on coffee for said customer
            for order in Order.all:
                if(order.customer == customer and order.coffee == coffee):
                    cur_total += order.price
            #compare to previous values, update if needed
            if(cur_total > ret_customer_total):
                ret_customer = customer 
                ret_customer_total = cur_total 
        #return customer
        return ret_customer


    @property 
    def name(self):
        return self._name 
    @name.setter 
    def name(self, new_name):
        if(isinstance(new_name, str) and 1 <= len(new_name) <= 15):
            self._name = new_name 
        else: 
            raise Exception('something went wrong setting customer name')
    

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
        if(isinstance(new_price, float) and 1.0 <= new_price <= 10.0 and not hasattr(self, 'price')):
            self._price = new_price 
        else: 
            print('couldnt set order price property')

    def __repr__(self):
        return f'<Order customer={self.customer} price={self.price} coffee={self.coffee} />'