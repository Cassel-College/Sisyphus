#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os

from frame.log.log4py import print_log
from tools.shell_box.v1.shell_tool import ShellTool


def create_folder(folder_path: str) -> bool:
    
    if check_folder_path_existed(folder_path=folder_path):
        print_log(log=f"Folder path: {folder_path} was existed.", level="INFO")
        return True
    shell = f"mkdir -p {folder_path}"
    shell_tool = ShellTool()
    shell_tool.run(cmd=shell)
    create_folder_success = check_folder_path_existed(folder_path=folder_path)
    if check_folder_path_existed:
        print_log(log="Folder create success.", level="INFO")
    else:
        print_log(log="Folder create error.", level="ERROR")
    return create_folder_success


def check_folder_path_existed(folder_path: str) -> bool:
    
    print_log(log=f"Check folder path: {folder_path} was existed?", level="DEBUG")
    folder_path_existed = False
    if os.path.isdir(folder_path):
        folder_path_existed = True
        print_log(log="Existed!", level="INFO") 
    else:
        print_log(log="Folder not existed.", level="INFO")
    return folder_path_existed


def check_folder_empty(folder_path: str) -> bool:
            
    print_log(log=f"Check folder empty?", level="ERROR")
    
    return True