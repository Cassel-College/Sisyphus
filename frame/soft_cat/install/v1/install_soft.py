#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from frame.log.log4py import print_log
from model.soft.v1.soft_model import SoftModel


def apt_get_update() -> str:
    
    name = 'apt-get'
    print_log(log=f"开始更新{name}", level="DEBUG")
    shell = f'{name} update'


def install_soft(soft: SoftModel) -> str:
    
    print_log(log=f"开始安装{soft.name}", level="DEBUG")
    shell = brew_install_soft_shell(soft=soft)
    


def brew_install_soft_shell(soft: SoftModel) -> str:
    
    if soft.drive == 'default':
        soft.drive = 'brew'
    shell = f"{soft.drive} install {soft.name}"
    return shell





