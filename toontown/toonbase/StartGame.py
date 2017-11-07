import traceback


import __builtin__
import time
import os
import sys
import random
class game(object):
    name = 'toontown'
    process = 'client'
__builtin__.game = game()
loadPrcFile('config/toontown.prc')

try:
    run()
except:
    traceback_info = traceback.format_exc()
else:
    traceback_info = 'Program crashed but no error was found'
finally:
    print(traceback_info)