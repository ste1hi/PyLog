import time
import traceback
import sys
sys.path.append("../")


class PyLog:

    def __init__(self, ifprint=1, path="./log.log"):
        self.ifprint = ifprint
        self.path = path
        self.code = self.__init__.__code__
        self.file_name = traceback.extract_stack()[1][0].split("/")[-1]\
            .split(".py")[0]

    def Logger(self, vaule, model):

        # get data
        hour, minu, sec = self.get_time()
        self.fucation = traceback.extract_stack()[1][2]
        # acill color
        if model == "INFO":
            color = "\033[0;32mINFO\033[0m"
        elif model == "WARNING":
            color = "\033[1;33mWARNING\033[0m"
        elif model == "ERROR":
            color = "\033[0;31mERROR\033[0m"
        else:
            raise AttributeError("Logger has no attribute '{0}'".format(model))
        # show infromation
        word = "[{0}][{1}:{2}:{3}][{4}/{5}]:{6}"\
            .format(self.file_name, hour, minu, sec,
                    self.fucation, color, vaule)
        word1 = "[{0}][{1}:{2}:{3}][{4}/{5}]:{6}"\
            .format(self.file_name, hour, minu, sec,
                    self.fucation, model, vaule)
        if self.ifprint == 1:
            print(word)
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
