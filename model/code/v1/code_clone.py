#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from frame.log.log4py import print_log
from model.code.v1.code import Code
from tools.shell_box.v1.shell_tool import ShellTool
from tools.folder_box.v1.folder_box import check_folder_path_existed, create_folder

def clone_code_core(local_path: str, code: Code) -> bool:
    
    print_log(log=f"开始clone代码到{local_path}.", level="DEBUG")
    clone_success = False
    
    if not check_folder_path_existed(folder_path=local_path):
        if not create_folder(folder_path=local_path):
            print_log(log=f"Create target folder path error! folder path: {local_path}.", level="ERROR")
            return clone_success

    print_log(log="", level="INFO")
    engine = "git clone"
    branch = f"-b {code.branch}"
    if code.branch is "main" or code.branch is "master":
        branch = ""
    shell = f"{engine} {branch} {code.url}"
    shell_tool = ShellTool()
    shell_tool.run(cmd=shell)
    
    return clone_success


def check_git_clone_success(local_path: str, code: Code) -> bool:
    
    clone_success = False
    return clone_success
    
