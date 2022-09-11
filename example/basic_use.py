import sys
sys.path.append(".")
from pylog import PyLog


def aa():
    log = PyLog()
    log.logger("ddd", "W")


aa()
