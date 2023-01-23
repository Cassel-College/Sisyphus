#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from frame.log.log4py import print_log
from model.soft.v1.soft_model import SoftModel


def get_soft_version(soft: SoftModel) -> str:
    
    print_log(log=f"查看{soft.name}版本", level="DEBUG")
    shell = f"{soft.name} --version 1>&2"
    version_info = ''
    print(shell)
    return version_info
    

def has_install(soft: SoftModel) -> bool:
    
    version = get_soft_version(soft=soft)
    if version:
        return True
    return False
    