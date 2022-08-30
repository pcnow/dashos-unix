import os
import time
from bin import shell

def kernel():
    print("dash_CORE is loading")
    time.sleep(2)
    os.system('clear')
    while True:
        shell.shell()
