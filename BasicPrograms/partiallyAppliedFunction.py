#%%
from functools import partial

def add(a:int ,b:int)->int:
    return a+b

add5= partial(add,a=5) 

print(add5(b=10))
# %%

add10=partial(add,b=10)
print(add10(10))
# %%
