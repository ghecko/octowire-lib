import os
import platform


# Common Colors
class Colors:
    if "Windows" in platform.system() and "WT_SESSION" not in os.environ:
        import colorama
        from colorama import Fore, Style

        colorama.init()
        HEADER = Fore.LIGHTMAGENTA_EX
        OKBLUE = Fore.BLUE
        OKGREEN = Fore.GREEN
        WARNING = Fore.YELLOW
        FAIL = Fore.RED
        ENDC = Fore.RESET
        BOLD = Style.BRIGHT
        UNDERLINE = ""
    else:
        HEADER = '\x1b[95m'
        OKBLUE = '\x1b[94m'
        OKGREEN = '\x1b[92m'
        WARNING = '\x1b[93m'
        FAIL = '\x1b[91m'
        ENDC = '\x1b[0m'
        BOLD = '\x1b[1m'
        UNDERLINE = '\x1b[4m'
