# %%
class Parent():
    def __init__(self):
        self.public_var="Public"
        self._protected_var="Protected"
        self.__private_var="Private"

    def access_from_same_class(self):
        print("Accessing from same class:")
        print(self.public_var)          # Accessible
        print(self._protected_var)      # Accessible
        print(self.__private_var)       # Accessible

class Child(Parent):
    def access_from_child_class(self):
        print("Accessing from child class:")
        print(self.public_var)          # Accessible
        print(self._protected_var)      # Accessible
        #print(self.__private_var)     # Not Accessible    

# %%
class Stranger():
    def access_from_stranger_class(self):
        parent = Parent()
        print("Accessing from stranger class:")
        print(parent.public_var)          # Accessible
        print(parent._protected_var)      # Not Accessible
        print(parent._Parent__private_var)       
        print(parent.__private_var) # Not Accessible

# %%
parent = Parent()
parent.access_from_same_class()
child = Child()
child.access_from_child_class()
#%%
stranger = Stranger()
stranger.access_from_stranger_class()

    
# %%
