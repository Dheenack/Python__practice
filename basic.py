# %%
print("hello")
# %%
# ## variables and datatypes
a:int=5
b:str="hello"
c:bool=True
d:float=20.6
for i in [a,b,c,d]:
    print(f"Type: {type(i)}\nValue:{i}")
# %%
# ##variable scope
def hello(name:str)->None:
    print(name,"hello")

hello("Yuvha")
# print(name) produces definition error
# %%
# ## Input Handling
a:str=input("enter your input:")
print(a)
b:int=int(input("enter an integer"))
print(b,"\nEnter a space seperated list of numbers")
c:list=list(map(int, input().split()))
print(c)
# %%
# ## cmd line arguements
import sys
name:str=sys.argv[1]
print(name)
