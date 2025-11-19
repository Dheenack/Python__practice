# %%
file=open("sample.txt","r" )
content=file.read()
print(content)
file.close()


# %%
file=open("sample.txt","a+")
file.write("\nAbracadabra")
print(file.read())
file.close()
# %%
