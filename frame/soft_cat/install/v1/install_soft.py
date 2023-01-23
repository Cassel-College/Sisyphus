#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from frame.log.log4py import print_log
from model.soft.v1.soft_model import SoftModel
from tools.shell_box.v1.shell_tool import ShellTool

def apt_get_update() -> str:
    
    name = 'apt-get'
    print_log(log=f"开始更新{name}", level="DEBUG")
    shell = f'{name} update'
    shell_tool = ShellTool()
    a = shell_tool.run(cmd=shell, not_print=True)
    print(a)
    return a    


def install_soft(soft: SoftModel) -> str:
    
    print_log(log=f"开始安装{soft.name}", level="DEBUG")
    # shell = brew_install_soft_shell(soft=soft)
    shell = apt_get_install_soft_shell(soft=soft)
    shell_tool = ShellTool()
    a = shell_tool.run(cmd=shell)
    print(a)
    return a  


def brew_install_soft_shell(soft: SoftModel) -> str:
    
    if soft.drive == 'default':
        soft.drive = 'brew'
    shell = f"{soft.drive} install {soft.name}"
    return shell


def apt_get_install_soft_shell(soft: SoftModel) -> str:
    
    if soft.drive == 'default':
        soft.drive = 'apt-get'
    shell = f"{soft.drive} install {soft.name}"
    if soft.drive == 'shell':
        shell = soft.shell
    return shell