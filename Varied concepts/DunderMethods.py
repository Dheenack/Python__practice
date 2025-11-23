# %%
from typing import Self
class Car:
    def __init__(self,brand:str,horsepower:int)->None:
        self.brand:str=brand
        self.horsepower:int=horsepower

    
    def __str__(self)->str:
        return f"Dunder method of tostring for current object: {self.brand}, {self.horsepower}"
    
    def __add__(self,other:Self)->str: #* dunder method for multiple objects
        return f"{self.brand} & {other.brand}"
    
# %%
volvo:Car=Car("volvo",123)
print(volvo)

Audi:Car=Car("Audi",100)

print(volvo+Audi)