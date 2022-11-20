import sys
import os
# Import package in vscode
sys.path.append(os.path.dirname(os.path.dirname
                (os.path.abspath(__file__))))
from pylog import pylog


def aa():
    log = pylog.PyLog()
    log.logger("TEST", "w")


aa()
