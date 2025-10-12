# %%
def greet()->None:
    print("hello Yuvha")
greet()

# %%
def greet(name)->None:
    print(f"hello,{name}")
greet("Yuvha")

# %%
def add(*a)->int:
    s=0
    for i in a:
        s += i
    return s

add(1,2,4,2)
# %%
def greet_custom(name="Yuvha")->None:
    print("hello",name)
greet_custom()
greet_custom("Swathi akka")
# %%
def details(**data)->None:
    for key,value in data.items():
        print(f"{key}:{value}")
details(name="Yuvha",age=21)
# %%
