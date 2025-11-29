def add(x:int,y:int)->int:
    try:
        if(type(x)!=int or type(y)!=int):
            raise Exception
        return x+y
    except Exception:
        return None