from bd import Connect

c = Connect()


def login():
    value = c.log()
    menu = (input('login:\n'), int(input('password:\n')))
    if menu in value:
        print('ok', bool(True))
        return True
    else:
        print('error password', bool(False))
        return False


