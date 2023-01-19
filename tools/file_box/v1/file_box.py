import os

class FileBox:
    
    def __init__(self) -> None:
        pass
    
    @classmethod
    def read(cls, file_path: str) -> str:
        
        file_info = ''
        if not os.path.isfile(file_path):
            return file_info
        with open(file_path, 'r') as file:
            file_info = file.read()
        return file_info


