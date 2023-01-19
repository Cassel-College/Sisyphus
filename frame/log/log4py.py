#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from model.log.v1.log_model import LogModel


def print_log_model(log_model: LogModel):
    
    print(log_model.info)


def print_log(log: str, path: str="", level: str="DEBUG"):
    
    log_model = LogModel(info=log, level=level, path=path)
    print_log_model(log_model=log_model)
    