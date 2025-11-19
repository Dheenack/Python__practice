# %%
# class example
class Greet():
    def greet(greet_class)->None:
        print("Hello")
obj=Greet()
obj.greet()
# %%
class Animal():
    def __init__(self,species,name)->None:
        self.species:str=species
        self.name:str=name
    def get_name(self)->str:
        #print(f"Name of the animal: {self.name}")
        return self.name
animal:Animal=Animal("Dog","Sekar")
name:str=animal.get_name()
# %%
