

def line(info: str, length: int=120) -> str:
    
    return info


def to_color(info: str, color: str='red') -> str:
    
    begin_color = '\033[1;31m'
    end_color = '\033[0m'
    info_with_color = "{}{}{}".format(begin_color, info, end_color)
    return info_with_color
    
    