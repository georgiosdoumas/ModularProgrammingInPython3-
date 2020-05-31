global cur_user
global login_hook 
cur_user = None
login_hook = None

def set_login_hook(hook):
    global login_hook
    login_hook = hook

def is_password_correct(u, p):
    """ Very simple function just for testing. 2 hardcoded username/pass """
    if (u == 'george' and p == 'geopas') or (u == 'mary' and p == 'marpas'):
        return True
    return False

def login(username, password):
    if is_password_correct(username, password):
        global cur_user 
        cur_user = username
        print("Successfully logged in as:", cur_user)
        global login_hook
        if  login_hook != None:
            set_login_hook(username)
        return True
    else:
        return False

def logout():
    global cur_user 
    cur_user = None
