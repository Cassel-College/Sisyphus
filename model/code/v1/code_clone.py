#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os

from frame.log.log4py import print_log
from model.code.v1.code import Code
from tools.shell_box.v1.shell_tool import ShellTool
from tools.folder_box.v1.folder_box import check_folder_path_existed, create_folder, check_folder_empty


def clone_code_core(local_path: str, code: Code) -> bool:
    
    clone_success = False
    print_log(log="", level="INFO")
    code_path = f"cd {local_path} && "
    engine = "git clone "
    branch = f"-b {code.branch} "
    if code.branch in ["main", "master", "None"]:
        branch = ""
    return_script_path = " && cd -"
    shell = f"{code_path}{engine}{branch}{code.url}{return_script_path}"
    shell_tool = ShellTool()
    shell_tool.run(cmd=shell)
    return clone_success


def check_code_folder(folder_path: str, project_name: str) -> bool:
    
    print_log(log="Check code folder: ", level="DEBUG")
    check_result = False
    project_path = os.path.join(folder_path, project_name)
    if not check_folder_path_existed(folder_path=project_path):
        if not create_folder(folder_path=project_path):
            print_log(log=f"Create target folder path error! folder path: {folder_path}.", level="ERROR")
            return check_result
        else:
            print_log(log="Code folder is created!", level="DEBUG")
            check_result = True
    else:
        print_log(log="Target folder was existed!", level="INFO")
        if check_folder_empty(folder_path=project_path):
            print_log(log="Target folder is empty.", level="INFO")
            check_result = True
        else:
            print_log(log="Target folder is not empty.", level="ERROR")
    return check_result


def clone_code(local_path: str, code: Code) -> bool:
    
    print_log(log=f"开始clone代码到{local_path}.", level="DEBUG")
    clone_success = False
    if check_code_folder(folder_path=local_path, project_name=code.project_name):
        clone_success = clone_code_core(local_path=local_path, code=code)
        if clone_success:
            clone_success = check_git_clone_success(local_path=local_path, code=code)
    return clone_success


def check_git_clone_success(local_path: str, code: Code) -> bool:
    
    print_log(log="Check whether the code was success?", level="ERROR")
    clone_success = False
    
    if clone_code:
        print_log(log="Clone code success.", level="DEBUG")
    else:
        print_log(log="Clone code error!", level="ERROR")
    return clone_success
    
