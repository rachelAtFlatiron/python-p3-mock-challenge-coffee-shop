#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee

if __name__ == '__main__':
    mocha = Coffee('mocha')
    latte = Coffee('latte')
    espresso = Coffee('espresso')
    decaf = Coffee('decaf')

    tim = Customer('tim')
    harry = Customer('harry')
    leia = Customer('leia')
    
    

    o1 = Order(tim, mocha, 3.0) # uses __init__ directly
    o2 = Order(tim, mocha, 5.0)
    o3 = Order(harry, decaf, 10.0)
    o4 = Order(leia, latte, 10.0)
    o5 = Order(leia, mocha, 3.0)
    o6 = leia.create_order(mocha, 9.0) # goes through Customer instance

    ipdb.set_trace()

