import login


def do_register(login, password):
    if login == "vasya@gmail.com" and password == "123456":
        print("Success")
    else:
        print("Try again")

do_register(login.login, login.password)