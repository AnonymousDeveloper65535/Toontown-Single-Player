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
from toontown.launcher.DummyLauncher import DummyLauncher  
launcher = DummyLauncher()
__builtin__.launcher = launcher
launcher.set_registry('EXIT_PAGE', 'normal')
poll_delay = 0.5
while not launcher.get_game2_finished:
    time.sleep(poll_delay)
print('Toontown is starting')
from pandac.PandaModules import *
    
try:
    run()
except:
    traceback_info = traceback.format_exc()
else:
    traceback_info = 'Program crashed but no error was found'
finally:
    print(traceback_info)
