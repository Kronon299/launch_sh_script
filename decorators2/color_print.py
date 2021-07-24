import functools
from colorama import Fore, Style


def color_print_method(color):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            color_codes = {'BLACK': Fore.BLACK,
                           'RED': Fore.RED,
                           'GREEN': Fore.GREEN,
                           'YELLOW': Fore.YELLOW,
                           'BLUE': Fore.BLUE,
                           'MAGENTA': Fore.MAGENTA,
                           'CYAN': Fore.CYAN,
                           'WHITE': Fore.WHITE,
                           }
            if color.upper() in color_codes:
                arg = color_codes[color.upper()]
            # elif color.upper() == 'BLACK':
            #     arg = Fore.BLACK
            # elif color.upper() == 'RED':
            #     arg = Fore.RED
            # elif color.upper() == 'GREEN':
            #     arg = Fore.GREEN
            # elif color.upper() == 'YELLOW':
            #     arg = Fore.YELLOW
            # elif color.upper() == 'BLUE':
            #     arg = Fore.BLUE
            # elif color.upper() == 'MAGENTA':
            #     arg = Fore.MAGENTA
            # elif color.upper() == 'CYAN':
            #     arg = Fore.CYAN
            # elif color.upper() == 'WHITE':
            #     arg = Fore.WHITE
            else:
                arg = Fore.RESET
            return f'{arg}{result}{Style.RESET_ALL}'
        return wrapper
    return decorator
