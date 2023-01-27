#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from frame.log.log4py import print_log


class Code:
    
    def __init__(self, project_name: str=None, url: str=None, branch: str=None) -> None:
        
        self.project_name = project_name
        self.url = url
        self.branch = branch
        
    def show(self):
        
        print(self.project_name)
        print(self.branch)
        print(self.url)
    

def create_code(info: dict) -> Code:
    
    project_name = info.get("project_name")
    url = info.get("url")
    branch = info.get("branch")
    code = Code(project_name=project_name, url=url, branch=branch)
    return code