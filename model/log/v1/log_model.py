

class LogModel:
    
    def __init__(self, info: str, path: str, level: str="INFO"):
        self.level = level
        self.info = info
        self.path = path

    def write_log(self):
        with open(self.path, 'a+') as f:
            f.write(f'[{self.level}] {self.info}')
            
    def filter_log(self, filter_level):
        if self.level != filter_level:
            return
        self.write_log()
