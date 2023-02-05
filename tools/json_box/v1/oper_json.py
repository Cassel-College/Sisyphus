#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from frame.log.log4py import print_log


def add(obj1, obj2):
    
    print_log()
    return obj1 + obj2


def diff(obj1, obj2):
    
    pass


def old(obj1, obj2):
    
    return obj1


oper_type = {
    "add": add,
    "diff": diff,
    "old": old
}


def oper(obj1, obj2, ploy):
    
    if isinstance(ploy, dict):
        return oper_json(obj1=obj1, obj2=obj2, ploy=ploy)
    if isinstance(ploy, str):
        if ploy in oper_type.keys():
            func = oper_type.get(ploy)
            return func(obj1, obj2)
        else:
            print_log(log="无定义操作", level="ERROR")
    return None


def oper_json(obj1: dict, obj2: dict, ploy: dict) -> dict:
    
    print_log(log="", level="DEBUG")
    
    new_obj = {}
    for key_word in ploy:
        item1 = None
        item2 = None
        item_ploy = ploy.get(key_word)
        if key_word in obj1.keys() and key_word in obj2.keys():
            item1 = obj1.get(key_word)
            item2 = obj2.get(key_word)
        new_value = oper(obj1=item1, obj2=item2, ploy=item_ploy)
        new_obj[key_word] = new_value
    return new_obj
            

#Test
def pp():
    
    ploy = {
        "a": "add",
        "b": "old"
    }

    a = {
        "a": 123,
        "b": "abc",
        "c": True
    }

    b = {
        "a": 123,
        "b": "abcpp",
        "c": True
    }
    aa = oper_json(obj1=a, obj2=b, ploy=ploy)

    print(aa)
     
