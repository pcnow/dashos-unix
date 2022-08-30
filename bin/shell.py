from conf import plist
from conf import userlist
from conf import osconf
import time
import os


def shell():
    print("dash_SHELL")
    print("v.0.1")

    userlist.users()
    userlist.rights()
    osconf.name()

    time.sleep(1)
    while True:
        print(userlist.curuser, end="")
        print("@", end="")
        print(osconf.pcname, end="")
        print(userlist.currights, end=" ")
        global com
        com = input()
        if com == "help":
            print("help, sysinfo, shinfo, kernel, calc, clear, pwd, mkdir, ls, su, pcname, exit")
        if com == "sysinfo":
            print("Dash OS")
            print("v.0.1")
            print("by pcnow")
        if com == "shinfo":
            print("dash_SHELL")
            print("v.0.1")
            print("by pcnow")
        if com == "kernel":
            print("dash_CORE for Python Interpretator")
            print("v.0.1")
        if com == "clear":
            os.system('clear')
        if com == "pwd":
            path = os.getcwd()
            print(path)
        if com == "mkdir":
            dirname = input("Name of directory: ")
            if os.path.exists(dirname):
                print("Directory exist!")
            if not os.path.exists(dirname):
                os.mkdir(dirname)
                print("Directory created")
        if com == "ls":
            lsd = os.listdir()
            print(lsd)
        plist.programs()
        if com == "exit":
            exit()
