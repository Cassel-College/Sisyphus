#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from frame.log.log4py import print_log
from tools.file_box.v1.file_box import FileBox
from tools.json_box.v1.json_box import JsonBox

def start():
    
    print_log(log="开始执行", level="DEBUG")
    
    print_log(log="开始读取策略文件", level="DEBUG")
    file_path = './template.json'
    info = FileBox.read(file_path=file_path)
    json_box = JsonBox(json_string=info)
    temp = json_box.get_all()
    print(type(temp))
    print(temp)
    softs = json_box.get_value("soft")
    for item in softs.keys():
        soft = softs.get(item)
        print(soft)
        
    print_log(log="开始探测环境", level="DEBUG")
    
    print_log(log="检测包管理软件是否安装？", level="DEBUG")
    
    print_log(log="检测包管理软件是否需要升级？", level="DEBUG")
    
    print_log(log="开始安装软件", level="DEBUG")
    
    print_log(log="开始安装python包", level="DEBUG")
    
    print_log(log="开始使用pip安装python包", level="DEBUG")
    
    print_log(log="开始设置文件夹目录", level="DEBUG")
    
    print_log(log="开始恢复文件", level="DEBUG")
    
    
if __name__ == "__main__":
    
    start()
