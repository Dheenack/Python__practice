#%%
## Anonymous function

square:int = lambda x:x*x
print(square(2))

# %%

## map funtion

names:list=["Yuvha","swathi","Dheena"]
upper_names:list=list(map(lambda x: x.upper(),names))
print(upper_names)


# %%
## Filter functions

names:list=["yuvha","swathi","dheena"]
name_ends_with_a:list = list(filter(lambda x:x.lower()[-1]=="a",names))
print(name_ends_with_a)

#%%
# reduce funtions
from functools import reduce

names:list[str]=["yuvha","swathi","dheena"]
all_names=reduce(lambda a,b : f"{a} {b}", names)
print(all_names)
# %%
numbers:list[int] = range(1,11)
total_numbers= reduce(lambda x,y:x+y,numbers)
print(total_numbers)
# %%
