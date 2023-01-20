#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import subprocess

from frame.log.log4py import print_log


class ShellTool:
    
    def __init__(self) -> None:
        
        pass
    
    def run(cmd: str=None, stderr: bool=True) -> str:
        
        result = subprocess.run(args=cmd, timeout=300, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if stderr:  
            return str(result.stdout.decode('utf-8'))
        return str(result.stderr.decode('utf-8'))
    
        
        