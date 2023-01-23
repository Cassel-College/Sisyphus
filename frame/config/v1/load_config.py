#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from frame.log.log4py import print_log
from tools.file_box.v1.file_box import FileBox
from tools.json_box.v1.json_box import JsonBox


class LoadConfig:
    
    def __init__(self) -> None:
        pass
    
    @classmethod
    def read_config_file(cls, config_path: str) -> str:
        
        info = FileBox.read(config_path)
        if not info:
            print_log(log="Config file was error.", level="ERROR")
        return info
    
    @classmethod
    def load(cls, config_path: str) -> dict:
        
        info = cls.read_config_file(config_path=config_path)
        config_map = JsonBox(json_string=info)
        return config_map
    
    @classmethod
    def get_config(cls, config_map: dict, name: str) -> str:
    
        value = ""
        if name in config_map.keys():
            value = config_map.get(name)
        else:
            print_log(log="", level="ERROR")
        return value
    
    @classmethod
    def get_configs(cls, config_map: dict, names: list) -> list:
        
        values = []
        for name in names:
            values.append(cls.get_config(config_map=config_map, name=name))
        return values
    