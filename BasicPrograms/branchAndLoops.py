# %%
num=int(input("enter a number"))
if(num==0): print("zero")
elif(num<0): print("negative num")
else: print("positive")
# %%
print("odd") if(num&1) else print("even")
# %%
# ## for loop

for i in range(1,10,2):
    print(i)
# %%
i:int=0
while(i<5):
    print(i,end=" ")
    i+=1
# %%
# List comprehension
sq_list=[n**2 for n in range(1,10)]
print(sq_list)
# %%
