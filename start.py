#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from frame.log.log4py import print_log
from frame.soft_cat.check_version.v1.check_version import has_install
from frame.soft_cat.install.v1.install_soft import install_soft
from model.soft.v1.soft_factory import create_soft
from tools.file_box.v1.file_box import FileBox
from tools.json_box.v1.json_box import JsonBox
from tools.shell_box.v1.shell_tool import ShellTool


def start():
    
    q = ShellTool.run(cmd="pwd", stderr=True)
    a = ShellTool.run(cmd="cat /home/l.txt", stderr=True)
    z = ShellTool.run(cmd="cat /home/l.txt", stderr=False)
    print(q)
    print(a)
    print(z)
    print_log(log="开始执行", level="DEBUG")
    
    print_log(log="开始读取策略文件", level="DEBUG")
    file_path = './template.json'
    info = FileBox.read(file_path=file_path)
    json_box = JsonBox(json_string=info)

    softs = json_box.get_value("soft")
    install_softs = softs.get("install")
    for item in install_softs.keys():
        soft = install_softs.get(item)
        print(soft)
        a = create_soft(name=soft.get("name"),
                        version=soft.get("version"))
        a.show()
        if not has_install(soft=a):
            install_soft(soft=a)
        
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
