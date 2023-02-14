#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# from frame.log.log4py import print_log


def line(info: str, length: int=120) -> str:
    
    if len(info) < length:
        l = int((length - len(info)) / 2)
        line_str = "-" * l
        info = f"{line_str}{info}{line_str}"
    return info


def to_color(info: str, color: str='red') -> str:
    
    begin_color = '\033[1;31m'
    end_color = '\033[0m'
    info_with_color = "{}{}{}".format(begin_color, info, end_color)
    return info_with_color
    
    