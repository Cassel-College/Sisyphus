#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os

from frame.log.log4py import print_log
from model.code.v1.code import Code
from tools.shell_box.v1.shell_tool import ShellTool


def clone_code_core(local_path: str, code: Code) -> bool:
    
    print_log(log=f"开始clone代码到{local_path}.", level="DEBUG")
    clone_success = False
    
    print_log(log="Check local path was existed?", level="INFO")
    if not os.path.isdir(local_path):
        print_log(log=f"Target folder was not existed, path: {local_path}.", level="INFO")
        
    else:
        print_log(log="", level="")
    engine = "git clone"
    branch = f"-b {code.branch}"
    shell = f"{engine} {branch} {code.url}"
    
    return clone_success