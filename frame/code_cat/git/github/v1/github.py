#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from frame.config.v1.load_config import LoadConfig
from frame.log.log4py import print_log
from model.code.v1.code import create_code
from model.code.v1.code_clone import clone_code


def clone_code_from_github(info: dict) -> bool:
    
    print_log(log="Clone code from github.", level="DEBUG")
    clone_success = False
    
    local_path = info.get("local_path")
    code = create_code(info=info)
    code.show()
    if clone_code(code=code, local_path=local_path):
        print_log(log="Clone code success.", level="INFO")
        clone_success = True
    else:
        print_log(log="Clone code error.", level="ERROR")
    return clone_success

