#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class SoftModel:
    
    def __init__(self, name: str, version: str) -> None:
        
        self.name = name
        self.version = version
        
    def show(self):
        
        print(self.name)
        print(self.version)

        
        

