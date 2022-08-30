from bin import shell
from conf import userlist
from bin import calc
from bin import su
from bin import pcname

userlist.users()

def programs():
    if shell.com == "calc":
        calc.calc()
    if shell.com == "su":
        su.su()
    if shell.com == "pcname":
        if userlist.curuser == "root":
            pcname.pcname()

