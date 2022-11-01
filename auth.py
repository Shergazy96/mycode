from Login import login
from bd import Connect
from regis import Reg_is

c = Connect()


class Auth:
    auth = True
    while auth:
        print('1: войти\n2: регистрация ')
        menu = input('выберите: 1 или 2\n>')
        if menu == '1':
            if login():
                auth = False
            elif bool(False):
                auth = True
        elif menu == '2':
            if Reg_is():
                auth = False
            elif bool(False):
                auth = True


Auth()
