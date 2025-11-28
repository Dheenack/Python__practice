#%%
def fact(n:int)->int:
    if n>=0:
        if(n==0):
            return 1
        else:
            return n* fact(n-1)
    else:
        return -1
    
print(fact(5))
print(fact(0))
print(fact(-100))

#
# %%
print("hakuna ma tata🐗")
# %%
def countdown(n)->None:
    if n==0:
        print("hai hai! yokatta")
        return
    else:
        print(n)
        return countdown(n-1)
    
countdown(5)
# %%
