#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from frame.log.log4py import print_log
from model.soft.v1.soft_model import SoftModel
from tools.shell_box.v1.shell_tool import ShellTool


def apt_get_uninstall_soft_shell(soft: SoftModel) -> str:
    
    if soft.drive == 'default':
        soft.drive = 'apt-get'
    shell = f"{soft.drive} remove {soft.name} -y"
    return shell


def uninstall_soft(soft: SoftModel) -> str:
    
    print_log(log=f"开始移除{soft.name}", level="DEBUG")
    # shell = brew_install_soft_shell(soft=soft)
    shell = apt_get_uninstall_soft_shell(soft=soft)
    shell_tool = ShellTool()
    a = shell_tool.run(cmd=shell)
    print(a)
    return a

  