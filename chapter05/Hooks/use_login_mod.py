import login_module

def my_login_hook(username):
    if username == 'george':
        print("Hello George! You have email.")
    else:
        print("Good morning ", username, " do  you want to read your email?")

if __name__ == '__main__':
    user1 = 'george'
    pass1 = 'geopas'
    login_module.set_login_hook(my_login_hook) # I am not sure if this line should be here ....
    print("Before login, cur_user :", login_module.cur_user) 
    login_module.login(user1, pass1)
    print("After login, cur_user :", login_module.cur_user)
    #login_module.set_login_hook(my_login_hook)  # .... or here! I do not get a greeting  in any case
