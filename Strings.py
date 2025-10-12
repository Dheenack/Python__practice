# %%
name:str=input("Enter a name")
email=name.lower().replace(" ",".")+"@company.com"
print(email)
# %%
# split
id,domain=email.split("@")
print(f"id:{id},domain:{domain}")
# %%
## formatting methods
print(name.title())
# %%
print(name.lower())
print(name.upper())
print(name.capitalize())
print(name.casefold())
# %%
# reverse a string
print(f"reversed name: {name[::-1]}")
# %%
## comprehension handling
name:str= "Dheena Krishna"
initials=[i[0] for i in name.split(" ")]
print(" ".join(initials))
# %%
# word count
sent="we are learning python with a competition"
print(f"word count:{len(sent.split())}")
# %%
