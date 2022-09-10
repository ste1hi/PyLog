import os
import time
import traceback


class PyLog:

    def __init__(self, if_print=True, path="./log.log"):
        self.if_print = if_print
        self.path = path
        self.code = self.__init__.__code__
        self.file_name = traceback.extract_stack()[1][0].split("/")[-1]\
            .split(".py")[0]

    def logger(self, vaule, model, if_print=None):
        if if_print is not None:
            self.if_print = if_print
        # Get data
        hour, minu, sec = self.__get_time()
        self.fucation = traceback.extract_stack()[1][2]
        # Acill color
        if model == "I":
            color = "\033[0;32mINFO\033[0m"
            model = "INFO"
        elif model == "W":
            color = "\033[1;33mWARNING\033[0m"
            model = "WARNING"
        elif model == "E":
            color = "\033[0;31mERROR\033[0m"
            model = "ERROR"
        else:
            raise AttributeError(f"Logger has no attribute '{model}'")
        # Show infromation
        colorful_word = f"[{self.file_name}][{hour}:{minu}:{sec}]"\
            f"[{self.fucation}/{color}]:{vaule}"

        colorless_word = f"[{self.file_name}][{hour}:{minu}:{sec}]"\
            f"[{self.fucation}/{model}]:{vaule}\n"

        # Print massage
        if self.if_print:
            print(colorful_word)
        with open(self.path, "a") as f:
            f.write(colorless_word)
        return colorless_word

    def __get_time(self):  # pragma: no cover

        hour = time.localtime().tm_hour
        minu = time.localtime().tm_min
        sec = time.localtime().tm_sec
        if hour < 10:
            hour = f"0{hour}"
        if minu < 10:
            minu = f"0{minu}"
        if sec < 10:
            sec = f"0{sec}"
        return hour, minu, sec

    def clean(self, if_confirm=True):  # pragma: no cover
        if if_confirm:
            self.logger(f"Confim delete {self.path} ", "W", True)
            i = input("Please input Y/N:")
            if i == "Y" or i == "y" or i == "yes":
                os.remove(self.path)
            else:
                self.logger(f"Cancel delete {self.path} ", "E", True)
        else:
            os.remove(self.path)
