from conf import osconf

osconf.name()

def pcname():
    tochange = input("Введите имя компьютера: ")
    osconf.pcname = tochange