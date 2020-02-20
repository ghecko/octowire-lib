# -*- coding: utf-8 -*-

# Octowire library
# Copyright (c) Jordan Ovrè / Paul Duncan
# License: GPLv3
# Paul Duncan / Eresse <eresse@dooba.io>
# Jordan Ovrè / Ghecko <ghecko78@gmail.com


import shutil


from octowire.utils.Colors import Colors
from tabulate import tabulate


class Logger:
    """
    Manage terminal printing.
    """
    DEFAULT = 0
    ERROR = 1
    SUCCESS = 2
    INFO = 3
    RESULT = 4
    USER_INTERACT = 5
    HEADER = 6
    WARNING = 7

    def __init__(self):
        self.categories = [
            self._print_default,
            self._print_error,
            self._print_success,
            self._print_info,
            self._print_result,
            self._print_user_interact,
            self._print_header,
            self._print_warning
        ]

    def handle(self, text, level=DEFAULT):
        """
        This function prints in different colors a given string.
        :param text: The string to print on the console.
        :param level: The message category.
        :return: Nothing.
        """
        self.categories[level](text) if (level < len(self.categories)) else self.categories[self.DEFAULT](text)

    @staticmethod
    def _print_default(text):
        """
        Print without style.
        :param text: Message to be printed.
        :return: Nothing.
        """
        print(text)

    @staticmethod
    def _print_error(text):
        """
        Beautify error message.
        :param text: Message to be printed.
        :return: Nothing.
        """
        print("{}[-]{} {}".format(Colors.FAIL, Colors.ENDC, text))

    @staticmethod
    def _print_success(text):
        """
        Beautify success message.
        :param text: Message to be printed.
        :return: Nothing.
        """
        print("{}[+]{} {}".format(Colors.OKGREEN, Colors.ENDC, text))

    @staticmethod
    def _print_info(text):
        """
        Beautify info message.
        :param text: Message to be printed.
        :return: Nothing.
        """
        print("[*] {}".format(text))

    @staticmethod
    def _print_result(text):
        """
        Beautify result message.
        :param text: Message to be printed.
        :return: Nothing.
        """
        print("{}[+] {}{}".format(Colors.OKGREEN, text, Colors.ENDC))

    @staticmethod
    def _print_user_interact(text):
        """
        Beautify user interaction message.
        :param text: Message to be printed.
        :return: Nothing.
        """
        print("{}[*] {}{}".format(Colors.OKBLUE, text, Colors.ENDC))

    @staticmethod
    def _print_header(text):
        """
        Beautify header message.
        :param text: Message to be printed.
        :return: Nothing.
        """
        print("{}{}{}".format(Colors.BOLD, text, Colors.ENDC))

    @staticmethod
    def _print_warning(text):
        """
        Beautify warning message.
        :param text: Message to be printed.
        :return: Nothing.
        """
        print("{}[!] {}{}".format(Colors.WARNING, text, Colors.ENDC))

    @staticmethod
    def print_tabulate(data, headers):
        """
        Print data in a beautiful tab.
        :param data: List of lists.
        :param headers: The headers of the array table.
        :return: Nothing.
        """
        t_width, _ = shutil.get_terminal_size()
        if t_width >= 95:
            print("\n{}\n".format(tabulate(data, headers=headers, tablefmt="fancy_grid")))
        else:
            print("\n{}\n".format(tabulate(data, headers=headers, tablefmt="rst")))
