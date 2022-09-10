import os
import time
import traceback
import sys
sys.path.append("../")


class PyLog:

    def __init__(self, ifprint=True, path="./log.log"):
        self.ifprint = ifprint
        self.path = path
        self.code = self.__init__.__code__
        self.file_name = traceback.extract_stack()[1][0].split("/")[-1]\
            .split(".py")[0]

    def Logger(self, vaule, model, ifprint=None):
        if ifprint is not None:
            self.ifprint = ifprint
        # Get data
        hour, minu, sec = self.get_time()
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
            raise AttributeError("Logger has no attribute '{0}'".format(model))
        # Show infromation
        word = "[{0}][{1}:{2}:{3}][{4}/{5}]:{6}"\
            .format(self.file_name, hour, minu, sec,
                    self.fucation, color, vaule)
        word1 = "[{0}][{1}:{2}:{3}][{4}/{5}]:{6}\n"\
            .format(self.file_name, hour, minu, sec,
                    self.fucation, model, vaule)
        # Print massage
        if self.ifprint:
            print(word)
        with open(self.path,"a") as f:
            f.write(word1)
        return word1

    def get_time(self):

        hour = time.localtime().tm_hour
        minu = time.localtime().tm_min
        sec = time.localtime().tm_sec
        if hour < 10:
            hour = "0{0}".format(hour)
        if minu < 10:
            minu = "0{0}".format(minu)
        if sec < 10:
            sec = "0{0}".format(sec)
        return hour, minu, sec

    def clean(self,ifconfirm = True):
        if ifconfirm == True:
            self.Logger(f"Confim delete {self.path} ","W",True)
            a = input("Please input Y/N:")
            if a == "Y" or a == "y" or a == "yes":
                os.remove(self.path)
            else:
                self.Logger(f"Cancel delete {self.path} ","E",True)
        else:
            os.remove(self.path)