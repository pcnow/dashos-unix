import os
import time
from sysfiles import kernel

print("Dash OS Loader")
print("v.0.1")
time.sleep(2)
os.system('clear')

while True:
    kernel.kernel()
