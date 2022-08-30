def users():
    global user
    user = "pcnow"
    global root
    root = "root"
    global curuser
    curuser = user
def rights():
    global userr
    userr = "$"
    global rootr
    rootr = "#"
    global currights
    if curuser == user:
        currights = userr
    if curuser == root:
        currights = rootr

