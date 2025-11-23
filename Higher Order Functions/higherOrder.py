# %%
def gmail_(username:str,domain="gmail.com"):
    return f"{username}@{domain}"

def hotmail_(username:str,domain="hotmail.com"):
    return f"{username}@{domain}"

def outlook_(username:str,domain="outlook.com"):
    return f"{username}@{domain}"

def build_email(username:str,email_function):
    return email_function(username)

# %%
print(build_email("dheenakrishhna",outlook_))
print(build_email("yuvha",hotmail_))
# %%
