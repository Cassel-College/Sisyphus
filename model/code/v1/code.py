#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from frame.log.log4py import print_log


class Code:
    
    def __init__(self, project_name: str=None, url: str=None, branch: str=None, source: str=None) -> None:
        
        self.project_name = project_name
        self.url = url
        self.branch = branch
        self.source = source
        
    def show(self):
        
        print(self.source)
        print(self.project_name)
        print(self.branch)
        print(self.url)
    

def create_code(info: dict) -> Code:
    
    source = info.get("source")
    project_name = info.get("project_name")
    url = info.get("git_url")
    branch = info.get("branch")

    code = Code(project_name=project_name, url=url, branch=branch, source=source)
    return code