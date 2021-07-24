import functools
from colorama import Fore, Style


def color_print(color):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if color.upper == 'BLACK':
                arg = Fore.BLACK
            elif color.upper == 'RED':
                arg = Fore.RED
            elif color.upper == 'GREEN':
                arg = Fore.GREEN
            elif color.upper == 'YELLOW':
                arg = Fore.YELLOW
            elif color.upper == 'BLUE':
                arg = Fore.BLUE
            elif color.upper == 'MAGENTA':
                arg = Fore.MAGENTA
            elif color.upper == 'CYAN':
                arg = Fore.CYAN
            elif color.upper == 'WHITE':
                arg = Fore.WHITE
            else:
                arg = Fore.RESET
            return f'{arg}{result}{Style.RESET_ALL}'
        return wrapper
    return decorator
