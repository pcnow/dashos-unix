from conf import userlist

userlist.users()
userlist.rights()

def su():
    tochange = input("Введите имя пользователя: ")
    if tochange == userlist.user:
        userlist.curuser = userlist.user
    if tochange == userlist.root:
        userlist.curuser = userlist.root
    if userlist.curuser == userlist.user:
        userlist.currights = userlist.userr
    if userlist.curuser == userlist.root:
        userlist.currights = userlist.rootr
