
from frame.log.log4py import print_log

def start():
    
    print("k")
    print_log(log="开始执行", level="DEBUG")
    
    print_log(log="开始读取策略文件", level="DEBUG")
    
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
