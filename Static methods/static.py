# %%
class Myclass:
    def instance_method(self):
        print("instance method",self)
    
    @classmethod
    def class_method(cls):
        print("class method",cls)

    @staticmethod
    def static_method():
        print("static method")

#  %%
if __name__ == "__main__":
    obj = Myclass()
    obj.instance_method()  # instance method <__main__.Myclass object at ...>
    Myclass.class_method()  # class method <class '__main__.Myclass'>
    Myclass.static_method() # static method
# %%
