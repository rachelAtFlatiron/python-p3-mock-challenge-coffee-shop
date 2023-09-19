#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")

    c1 = Coffee('mocha')
    c2 = Coffee('latte')
    cu1 = Customer('frank')
    cu2 = Customer('annie')
    o1 = Order(cu1, c1, 3.0)
    o2 = Order(cu2, c2, 5.0)
    o3 = Order(cu2, c1, 5.0)
    ipdb.set_trace()
