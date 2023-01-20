#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from model.log.v1.log_model import LogModel
from tools.string_box.v1.string_box import to_color


def print_log_model(log_model: LogModel):
    
    info = to_color(info=log_model.info, color="red")
    print(info)


def print_log(log: str, path: str="", level: str="DEBUG"):
    
    log_model = LogModel(info=log, level=level, path=path)
    print_log_model(log_model=log_model)
    