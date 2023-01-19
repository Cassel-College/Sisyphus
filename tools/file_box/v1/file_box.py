#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os

from frame.log.log4py import print_log

class FileBox:
    
    def __init__(self) -> None:
        pass
    
    @classmethod
    def read(cls, file_path: str) -> str:
        
        print_log(log="获取文件" + file_path + "信息", level="INFO")
        file_info = ''
        if cls.check_file_existed(file_path=file_path):
            with open(file_path, 'r') as file:
                file_info = file.read()
        return file_info
    
    @classmethod
    def check_file_existed(cls, file_path: str) -> bool:
        
        print_log(log="检查文件" + file_path + "是否存在？", level="INFO")
        if os.path.isfile(file_path):
            print_log(log="文件" + file_path + "存在", level="INFO")
            return True
        print_log(log="文件" + file_path + "不存在", level="ERROR")
        return False