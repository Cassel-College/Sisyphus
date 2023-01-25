#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from frame.log.log4py import print_log


class Code:
    
    def __init__(self) -> None:
        
        self.project_name = ''
        self.url = ''
        self.branch = ''
        
    def show(self):
        
        print(self.project_name)
        print(self.branch)
        print(self.url)
    
    