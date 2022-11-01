from bd import Connect

c = Connect()


def Reg_is():
    n = c.name()
    name = input('name:\n')
    password = int(input('password:\n'))
    if (name,) in n:
        print(f'занят {name}')
        return False
    else:
        print('ok')
        c.create(name, password, )
        return True




